async function utils_fetch(url, request_method, body_data = null,stringify = true,form=false) {
    function getCookie(name) {
        //example: to get csrf Token name must be set to 'csrftoken'
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    try {
        if (request_method === 'GET') {
            let headers = {
                'Content-Type': 'application/json'
            };
            const response = await fetch(url, { headers, });
            const response_json = await response.json();
            return response_json;
        } else if (request_method === 'DELETE') {
            const csrftoken_ = getCookie('csrftoken');
            const defaults = {
                'method': 'DELETE',
                'credentials': 'same-origin',
                'headers': new Headers({
                    'X-CSRFToken': csrftoken_,
                }),
            };
            const response = await fetch(url, defaults);
            return true;

        } else if (request_method === 'POST' || request_method === 'PUT' || request_method==='PATCH') {
            const csrftoken_ = getCookie('csrftoken');
            let contentType = form?'multipart/form-data;boundary=simple boundary':'application/json';
            //const urlencoded = new URLSearchParams(JSON.stringify(body_data));
            if (form){
                // // We need to add a boundary parameter to the header
                // // We assume the first valid-looking boundary line in the body is correct
                // // regex is from RFC 2046 appendix A
                // var boundaryCharNoSpace = "0-9A-Z'()+_,-./:=?";
                // var boundaryChar = boundaryCharNoSpace + ' ';
                // var re = new RegExp('^--([' + boundaryChar + ']{0,69}[' + boundaryCharNoSpace + '])[\\s]*?$', 'im');
                // var boundary = data.match(re);
                // if (boundary !== null) {
                //   contentType += '; boundary="' + boundary[1] + '"';
                // }
                // // Fix textarea.value EOL normalisation (multipart/form-data should use CR+NL, not NL)
                // data = data.replace(/\n/g, '\r\n');

                // Use the FormData API and allow the content type to be set automatically,
                // so it includes the boundary string.
                contentType=false;
            }
            const defaults = {
                'method': request_method,
                'credentials': 'same-origin',
                'headers': new Headers({
                    'X-CSRFToken': csrftoken_,
                }),
                'body': stringify?JSON.stringify(body_data):body_data,
            };
            contentType?defaults['headers'].append('Content-Type',contentType):false;
            const response = await fetch(url, defaults);
            return response;
        }
    } catch (err) { alert(err); return false }
}

interview_metadata = JSON.stringify({
    age:51,
    gender:"F",
    is_smoker:false,
    is_pregnant:true,
    is_obese:null,
    is_injured:null,
    has_hypertension:null,
})
utils_fetch("http://localhost:8000/api/v1/interviews/init/","POST");
utils_fetch("http://localhost:8000/api/v1/interviews/setMeta/995fc899-abde-49f3-b547-664bea20a35a/",
"POST",
body_data=interview_metadata
);