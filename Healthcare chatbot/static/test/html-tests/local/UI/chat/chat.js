function switch_vision(){
    let model = document.getElementById("svg-model-container");
    let history = document.getElementById("history-container");
    let btn = document.getElementById("switch_button");
    if (model.getAttribute("visible") == "false"){
        model.classList.remove("hidden");
        model.setAttribute("visible","true");

        history.classList.add("hidden");
        history.setAttribute("visible","false");

        btn.innerHTML = "History";
        
    }
    else if (model.getAttribute("visible") == "true"){
        history.classList.remove("hidden");
        history.setAttribute("visible","true");

        model.classList.add("hidden");
        model.setAttribute("visible","false");

        btn.innerHTML = "Choose<br/>Symptom";
    }
}

const symtoms_by_bodyPart = {
    head:[
        "headache",
        "Fever",
        "Dizzy",
        "hair loss",
    ],
    whole_head:[
        "swollen face",
        "Facial muscle weakness",
        "feeling sick",
    ],
    eyes:[
        "Eye pain",
        "Bloodshot eye",
        "yellow eyes",
    ],
    ears:[
        "earache",
        "ringin in ears",
    ],
    nose:[
        "Nose pain",
        "Nasal voce",
        "Nose bleed",
        "Snoring",
    ],
    oral_cavity:[
        "Bad breath",
        "Dry mouth",
        "Toothache",
    ],
    neck_or_throat:[
        "Sore throat",
        "painfull swallowing",
        "Cough",
    ],
    chest:[
        "Chest pain",
        "Palpitations",
    ],
    forearm:[
        "Pain in forearm",
        "Numbness",
        "Spasms in upper extremities",
        "Soreness",
    ],
    upper_arm:[
        "shoulder pain",
        "swollen shoulder",
    ],
    hand:[
        "wrist pain",
        "pain in fingers",
        "swollen wrist",
    ],
    elbow:[
        "elbow pain",
    ],
    thigh:[
        "swollen legs",
        "leg weakness",
    ],
    lower_back:[
        "lower back pain",
        "sudden back pain",
        "paraspinal tenderness",
    ],
    back:[
        "back pain",
        "Stiffness of spine",
    ],
}

function bodyPartSelected(event,bodyPart){
    let div = document.getElementById("symtoms-container");
    div.querySelector("#symtoms-label").innerText = bodyPart;
    div.classList.remove("hidden");
    div.style.display = "inline"
    div.style.position = "absolute";
    div.style.zIndex = "100";
    xPos = (event.x + window.scrollX);
    yPos = (event.y + window.scrollY);
    div.style.top = yPos + "px";
    div.style.left = xPos + "px";
    loadOptions("symtoms");
    function loadOptions(id){
        let select_box = document.getElementById(id);
        select_box.innerHTML = "<option value='' selected>-- Choose symptom --</option>"
        if (symtoms_by_bodyPart[bodyPart]){
        for (let i=0 ; i<symtoms_by_bodyPart[bodyPart].length;i++){
            //vulnerable change it to child + innerText
            let symptom = symtoms_by_bodyPart[bodyPart][i];
            select_box.innerHTML += `<option value="${symptom}">${symptom}</option>`
        }
        }
        else{
            select_box.innerHTML += `<option value="">To be filled ...</option>`
        }
    }
}

function addSymtoms(event){
    let symptom = event.target.value;
    
    document.getElementById("symtoms-container").classList.add("hidden");
    if (symptom){
        addMessage("i have "+symptom);
        //got rid of it in case the user made a miss input
        //communicate();
    }
}

function addMessage(message){
    document.getElementById("message-input").value = message;
}

const send_button = document.getElementById("send-message");
const CHATBOT_API = "http://localhost:8888/chatbot"
const ASUNA_IMAGE_LINK = "https://i.pinimg.com/originals/84/e6/2e/84e62e9a9418321fdf35810aa93c6419.jpg"
const msg_box = document.getElementById("message-box");
const MONTH = [ 'January',
'February',
'March',
'April',
'May',
'June',
'July',
'August',
'September',
'October',
'November',
'December' ]
function writeToMessageBox(message,source){
    var currentdate = new Date();

    let timeString = `${(currentdate.getHours()<10)?"0":""}${(currentdate.getHours()<=12)?currentdate.getHours():currentdate.getHours()-12}:`;
    timeString+= `${(currentdate.getMinutes()<10)?"0":""}${currentdate.getMinutes()} ${(currentdate.getHours()<12)?"AM":"PM"}  |  `;
    timeString+= `${MONTH[currentdate.getMonth()]} ${(currentdate.getDay()<10)?"0":""}${currentdate.getDay()}`
    
    if (message){
    if (source =="incomming"){
        msg_box.innerHTML +=`<div class="incoming_msg">
        <div class="incoming_msg_img"> 
            <img src="${ASUNA_IMAGE_LINK}" alt="Asuna"> 
        </div>
        <div class="received_msg">
          <div class="received_withd_msg">
            <p>${message}</p>
            <span class="time_date"> ${timeString}</span></div>
        </div>
      </div>`
    }
    else if(source =="outgoing") {
        msg_box.innerHTML +=`<div class="outgoing_msg">
        <div class="sent_msg">
          <p>${message}</p>
          <span class="time_date"> ${timeString}</span> </div>
      </div>
        `
    }
    }
}
const HISTORY_CONTAINER= document.getElementById("history-container");
function writeToInterviewBow(interview_id,date_string,results,is_active){
    HISTORY_CONTAINER.innerHTML+=`<div class="chat_list ${is_active?"active_chat":""}">
    <div class="chat_people">
      <div class="chat_img"> <img src="${ASUNA_IMAGE_LINK}" alt="Asuna"> </div>
      <div class="chat_ib">
        <h5>Interview ID: ${interview_id} <span class="chat_date">${date_string}</span></h5>
        <p>The results to this Intervew where: You might have ${results}</p>
      </div>
    </div>
      </div>`
}
async function communicate(){
    const input = document.getElementById("message-input");
    console.log(input);
    let message = input.value;
    input.value="";
    console.log(message);
    async function sendMessage(message){
        
        let resp = await fetch(CHATBOT_API,{
            method: 'POST',
            mode:"no-cors",
            headers:{
            'content-type':'application/json'
            },
            body: JSON.stringify({question:message})
        });
        try{
            return resp.json();
        }
        catch{
            return null
        }
    }
    writeToMessageBox(message,"outgoing");
    let response = await JSON.parse(sendMessage(message))
    console.log(response);
    if (response.illness){
         writeToMessageBox(`Here are the results:
         the illness is : ${response.illness}
         the probability is : ${response.probability}`,"incomming");
    }
    else{
        writeToMessageBox(response,"incomming");
    }
}
//writeToMessageBox("hello!","outgoing");
//writeToMessageBox("hello i'm assuna","incomming");
writeToInterviewBow("hjgs2g42s1gs25452s","JUNE 25","Familial nonhemolytic jaundice",true)
writeToInterviewBow("36qdjq1gs25452ddss","JUNE 24","Indigestion",false)
writeToInterviewBow("65q144sls2ddss5452","JUNE 23","Indigestion",false)


send_button.addEventListener('click',communicate);
document.getElementById("message-input").addEventListener('keypress',(e)=>{
    if (e.key =="Enter"){
        communicate();
    }
})
document.getElementById("switch_button").addEventListener('click',switch_vision);
document.querySelector(".inbox_chat").addEventListener('click',(e)=>{
    function is_parent(elt,parent){
        if (elt.parentElement == null){return false}
        else if (elt.isEqualNode(parent)){return true}
        else{return is_parent(elt.parentElement,parent)}
    }

    let svg_container =document.getElementById("svg-container");
    let div = document.getElementById("symtoms-container");
    if (((!is_parent(e.target,svg_container)) || e.target.tagName=="svg") && !is_parent(e.target,div) ){
        // you can also seach for 
        div.classList.add("hidden");
    }
})