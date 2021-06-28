// async function init_interview(){
//     const resp = await utils_fetch("http://localhost:8000/api/v1/interviews/init/","POST");
//     const obj = await resp.json();
//     document.getElementById("interview_id").innerText = obj.id;
//     return obj.id
// }
// document.getElementById("get-metadata").addEventListener('click',()=>{
//     document.getElementById("welcome").classList.add("hidden")
//     document.getElementById("meta").classList.remove("hidden")
// })

// document.getElementById("send-meta").addEventListener('click',(e,interview_id)=>{
//     e.preventDefault();
//     function clean(value){
//         if (value =="true") return true
//         else if (value =="false") return false
//         else if (value =="unknown") return null
//     }
//     const form = document.getElementById("meta-form");
//     const payload = {
//         age:form.querySelector("[name='age']").value,
//         gender:form.querySelector("[name='gender']").value,
//         is_smoker:clean(form.querySelector("[name='is_smoker']").value),
//         is_pregnant:clean(form.querySelector("[name='is_pregnant']").value),
//         is_obese:clean(form.querySelector("[name='is_obese']").value),
//         is_injured:clean(form.querySelector("[name='is_injured']").value),
//         has_hypertension:clean(form.querySelector("[name='has_hypertension']").value),
//     }
//     utils_fetch(`http://localhost:8000/api/v1/interviews/setMeta/${interview_id}/`,
//     "POST",
//     body_data=payload
//     ).then(()=>loadChat());
// })
