// document.querySelector("body").classList.remove();
// document.querySelector("#cover").classList.remove("cover-container",);
// document.querySelector("header").classList.add("nav-extra");
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
document.getElementById("switch_button").addEventListener('click',switch_vision);

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

// const send_button = document.getElementById("send-message");
// const CHATBOT_API = "http://localhost:8888/chatbot/"
// //const ASUNA_IMAGE_LINK = "https://i.pinimg.com/originals/84/e6/2e/84e62e9a9418321fdf35810aa93c6419.jpg";
// const ASUNA_IMAGE_LINK = IMG_URL;
// const msg_box = document.getElementById("message-box");
// const MONTH = [ 'January',
// 'February',
// 'March',
// 'April',
// 'May',
// 'June',
// 'July',
// 'August',
// 'September',
// 'October',
// 'November',
// 'December' ]
// function writeToMessageBox(message,source,date=null){
//     let currentdate;
//     if (date){ currentdate= date;}
//     else{currentdate = new Date();}

//     let timeString = `${(currentdate.getHours()<10)?"0":""}${(currentdate.getHours()<=12)?currentdate.getHours():currentdate.getHours()-12}:`;
//     timeString+= `${(currentdate.getMinutes()<10)?"0":""}${currentdate.getMinutes()} ${(currentdate.getHours()<12)?"AM":"PM"}  |  `;
//     timeString+= `${MONTH[currentdate.getMonth()]} ${(currentdate.getDay()<10)?"0":""}${currentdate.getDay()}`
    
//     if (message){
//     if (source =="incomming"){
//         msg_box.innerHTML +=`<div class="incoming_msg">
//         <div class="incoming_msg_img"> 
//             <img src="${ASUNA_IMAGE_LINK}" alt="Asuna"> 
//         </div>
//         <div class="received_msg">
//           <div class="received_withd_msg">
//             <p>${message}</p>
//             <span class="time_date"> ${timeString}</span></div>
//         </div>
//       </div>`
//     }
//     else if(source =="outgoing") {
//         msg_box.innerHTML +=`<div class="outgoing_msg" style="text-align:right;">
//         <div class="sent_msg">
//           <p>${message}</p>
//           <span class="time_date"> ${timeString}</span> </div>
//       </div>
//         `
//     }
//     }
// }
// const HISTORY_CONTAINER= document.getElementById("history-container");
// function writeToInterviewBow(interview_id,date_string,results,is_active){
//     HISTORY_CONTAINER.innerHTML+=`<div class="chat_list ${is_active?"active_chat":""}">
//     <div class="chat_people">
//       <div class="chat_img"> <img src="${ASUNA_IMAGE_LINK}" alt="Asuna"> </div>
//       <div class="chat_ib">
//         <h5>Interview ID: ${interview_id} <span class="chat_date">${date_string}</span></h5>
//         <p>The results to this Intervew where: You might have ${results}</p>
//       </div>
//     </div>
//       </div>`
// }
// async function saveMessage(interview_id,message,source){
//     let message_data = {
//         message:message,
//         date:(new Date().toISOString()),
//         source:source
//     }
//     const resp = await utils_fetch(`http://localhost:8000/api/v1/interviews/addMessage/${interview_id}/`,
//     "POST",
//     body_data=message_data);
//     if (resp.ok) return true
//     else return null
// }

// async function sendMessage(interview_id,message){
        
//     let resp = await fetch(CHATBOT_API,{
//         method: 'POST',
//         headers:{
//         'Content-Type':'application/json'
//         },
//         body: JSON.stringify({question:message})
//     });
//     if (saveMessage(interview_id,message,'I')){
//         try{
//             return resp.json();
//         }
//         catch{
//             return resp.text();
//         }
//     }
    
// }
// async function communicate(){
//     const input = document.getElementById("message-input");
//     let message = input.value;
//     input.value="";
//     const interview_id = INTERVIEW_ID;
//     writeToMessageBox(message,"outgoing");
//     let asuna_resp = await sendMessage(interview_id,message);
//     if (asuna_resp){
//         if (asuna_resp.response.illness){
//             // incomming for client = outgoing for server
//             const resp_message = `You might have ${asuna_resp.response.illness} 
//             with a likelyhood of ${asuna_resp.response.probability*100}%`
//             writeToMessageBox(resp_message,"incomming");
//             saveMessage(interview_id,resp_message,"O");
//         }
//         else{
//             writeToMessageBox(asuna_resp.response,"incomming");
//             saveMessage(interview_id,asuna_resp.response,"O");
//         }
//     }
// }
// writeToInterviewBow("hjgs2g42s1gs25452s","JUNE 25","Familial nonhemolytic jaundice",true)
// writeToInterviewBow("36qdjq1gs25452ddss","JUNE 24","Indigestion",false)
// writeToInterviewBow("65q144sls2ddss5452","JUNE 23","Indigestion",false)


// send_button.addEventListener('click',communicate);
// document.getElementById("message-input").addEventListener('keypress',(e)=>{
//     if (e.key =="Enter"){
//         communicate();
//     }
// })
// async function getResults(){
//     const message ="results"
//     let asuna_resp = await sendMessage(message);
//     if (asuna_resp.response.illness){
//         writeToMessageBox(`You might have ${asuna_resp.response.illness} 
//         with a likelyhood of ${asuna_resp.response.probability*100}%`,"incomming");
//     }
//     else{
//         writeToMessageBox(asuna_resp.response,"incomming");
//     }
// }

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
// document.getElementById("results_button").addEventListener("click",getResults);