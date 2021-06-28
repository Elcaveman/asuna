class InterviewWindow{
    constructor(chat_window){
        this.interview_id = null
        this.window_id = "interview-window"
        this.other_windows_ids=["chat-window",]
        this.sections_ids = ["welcome","meta"]
        this.chat_window = chat_window
        this.events_created = false
    }
    
    async init_interview(){
        const resp = await utils_fetch("http://localhost:8000/api/v1/interviews/init/","POST");
        const obj = await resp.json();
        document.getElementById("interview_id").innerText = obj.id;
        this.interview_id = obj.id;
    }
    welcome(){
        document.getElementById("get-metadata").addEventListener('click',()=>{
            document.getElementById("welcome").classList.add("hidden")
            document.getElementById("meta").classList.remove("hidden")
        })
    }
    meta(){
        let self = this;
        const id = this.interview_id;
        if (this.events_created==false){

            document.getElementById("send-meta").addEventListener('click',(e)=>{
            e.preventDefault();
            function clean(value){
                if (value =="true") return true
                else if (value =="false") return false
                else if (value =="unknown") return null
            }
            const form = document.getElementById("meta-form");
            const payload = {
                age:form.querySelector("[name='age']").value,
                gender:form.querySelector("[name='gender']").value,
                is_smoker:clean(form.querySelector("[name='is_smoker']").value),
                is_pregnant:clean(form.querySelector("[name='is_pregnant']").value),
                is_obese:clean(form.querySelector("[name='is_obese']").value),
                is_injured:clean(form.querySelector("[name='is_injured']").value),
                has_hypertension:clean(form.querySelector("[name='has_hypertension']").value),
            }
            console.log(payload);
            utils_fetch(`http://localhost:8000/api/v1/interviews/setMeta/${self.interview_id}/`,"POST",payload)
            .then(()=>self.chat_window.show_window());
            })
            this.events_created=true
        }
    }
    async show_window(){
        await this.init_interview();
        document.getElementById(this.window_id).classList.remove("hidden");
        for (let i=0;i<this.other_windows_ids.length;i++){
            document.getElementById(this.other_windows_ids[i]).classList.add("hidden");
        }
        this.meta();
        this.welcome();
    }
}

class ChatWindow{
    constructor(){
        this.selected_interview = null;
        this.window_id = "chat-window"
        this.other_windows_ids = ["interview-window",]
        this.send_button = document.getElementById("send-message");
        this.CHATBOT_API = "http://localhost:8888/chatbot/"
        this.ASUNA_IMAGE_LINK = IMG_URL;
        this.msg_box = document.getElementById("message-box");
        this.MONTH = [ 'January','February','March','April','May','June','July','August','September','October','November','December' ]
        this.HISTORY_CONTAINER= document.getElementById("history-container");
        this.events_created = false;
    }
    async get_interviews(){
        const resp = utils_fetch("http://localhost:8000/api/v1/interviews/","GET");
        return resp
    }
    writeToInterviewBox(interview_id,date_string,results){
        let chat_list = document.createElement("div");
        chat_list.setAttribute("interview_id",interview_id);
        chat_list.classList.add("chat_list");
        let self = this;
        chat_list.addEventListener("click",(e)=>{
            if (document.querySelector(".chat_list.active_chat")){
                document.querySelector(".chat_list.active_chat").classList.remove("active_chat");
            }
            chat_list.classList.add("active_chat");
            self.selected_interview = chat_list.getAttribute("interview_id");
            self.load_chat();
        })
        chat_list.innerHTML+=`
        <div class="chat_people">
          <div class="chat_img"> <img src="${this.ASUNA_IMAGE_LINK}" alt="Asuna"> </div>
          <div class="chat_ib">
            <h5>Interview ID: ${interview_id} <span class="chat_date">${date_string}</span></h5>
            <p>The results to this Intervew were: You might have ${results}</p>
          </div>
        </div>`
        this.HISTORY_CONTAINER.appendChild(chat_list);
    }

    async load_interviews(){
        this.HISTORY_CONTAINER.innerHTML = "";
        let interviews = await this.get_interviews();
        for (let i=0;i<interviews.length;i++){
            let dat = new Date(interviews[i].creation_date);

            this.writeToInterviewBox(
                interviews[i].interview_id,
                dat.toDateString(),
                interviews[i].results.illness
                );
        }
    }
    writeToMessageBox(message,source,date=null){
        let currentdate;
        if (date){currentdate= date;}
        else{currentdate = new Date();}
    
        let timeString = `${(currentdate.getHours()<10)?"0":""}${(currentdate.getHours()<=12)?currentdate.getHours():currentdate.getHours()-12}:`;
        timeString+= `${(currentdate.getMinutes()<10)?"0":""}${currentdate.getMinutes()} ${(currentdate.getHours()<12)?"AM":"PM"}  |  `;
        timeString+= `${this.MONTH[currentdate.getMonth()]} ${(currentdate.getDay()<10)?"0":""}${currentdate.getDay()}`
        
        if (message){
        if (source =="incomming"){
            this.msg_box.innerHTML +=`<div class="incoming_msg">
            <div class="incoming_msg_img"> 
                <img src="${this.ASUNA_IMAGE_LINK}" alt="Asuna"> 
            </div>
            <div class="received_msg">
              <div class="received_withd_msg">
                <p>${message}</p>
                <span class="time_date"> ${timeString}</span></div>
            </div>
          </div>`
        }
        else if(source =="outgoing") {
            this.msg_box.innerHTML +=`<div class="outgoing_msg" style="text-align:right;">
            <div class="sent_msg">
              <p>${message}</p>
              <span class="time_date"> ${timeString}</span> </div>
          </div>
            `
        }
        }
    }
    async saveMessage(message,source){
        let message_data = {
            message:message,
            date:(new Date().toISOString()),
            source:source
        }
        const resp = await utils_fetch(
            `http://localhost:8000/api/v1/interviews/addMessage/${this.selected_interview}/`,
            "POST",message_data);
        if (resp) return true
        else return null
    }
    async sendMessage(message){
        
        let resp = await fetch(this.CHATBOT_API,{
            method: 'POST',
            headers:{
            'Content-Type':'application/json'
            },
            body: JSON.stringify({question:message})
        });
        try{
            return resp.json();
        }
        catch{
            return resp.text();
        }
        }
    async communicate(){
        const input = document.getElementById("message-input");
        let message = input.value;
        input.value="";
        this.writeToMessageBox(message,"outgoing");
        let asuna_resp = await this.sendMessage(message);
        await this.saveMessage(message,"I");
        if (asuna_resp){
            if (asuna_resp.response.illness){
                // incomming for client = outgoing for server
                await utils_fetch(`http://localhost:8000/api/v1/interviews/saveResult/${this.selected_interview}/`,
                "POST",
                {result:asuna_resp.response});
                let disease = await utils_fetch(`http://localhost:8000/api/v1/diseases/${asuna_resp.response.illness}`,"GET");
                this.writeToMessageBox(`You might have ${asuna_resp.response.illness} 
                with a likelyhood of ${asuna_resp.response.probability*100}%`,"incomming");
                if (disease){
                    this.writeToMessageBox(`Symptoms:${disease.symptoms} `,"incomming");
                    this.writeToMessageBox(`Description:${disease.description} `,"incomming");
                    this.writeToMessageBox(`Treatement Metod:${disease.cure_method} `,"incomming");
                }
            }
            else{
                this.writeToMessageBox(asuna_resp.response,"incomming");
                this.saveMessage(asuna_resp.response,"O");
            }
        }
    }
    async load_chat(){
        //clean the chat
        this.msg_box.innerHTML = "";
        const reverse_dic = {"I":"outgoing","O":"incomming"}
        if(this.selected_interview){
            const resp = await utils_fetch(`http://localhost:8000/api/v1/interviews/${this.selected_interview}/`,"GET");
            
            if (this.selected_interview == resp.interview_id){
                for (let i=0;i<resp.chat_history.length;i++){
                    this.writeToMessageBox(resp.chat_history[i].message,
                        reverse_dic[resp.chat_history[i].source],
                        new Date(resp.chat_history[i].date)
                        )
                }
            }
            else{
                console.log(this.selected_interview,resp.interview_id)
            }
        }
        else{

        }
    }
    show_window(){
        document.getElementById(this.window_id).classList.remove("hidden");
        for (let i=0;i<this.other_windows_ids.length;i++){
            document.getElementById(this.other_windows_ids[i]).classList.add("hidden");
        }
        //link communication box with functionality
        this.manage_EventListener();
        this.load_interviews();
    }
    manage_EventListener(){
        if (this.events_created==false){
            let self = this;
            this.send_button.addEventListener('click',self.communicate);
            document.getElementById("message-input").addEventListener('keypress',(e)=>{
                if (e.key =="Enter"){
                    self.communicate();
                }
            })
            this.events_created = true;
        }
    }
}

let chat_window = new ChatWindow()
let interview_window = new InterviewWindow(chat_window)

chat_window.show_window();
document.getElementById("interview_creation").addEventListener("click",(e)=>{
    interview_window.show_window();
})