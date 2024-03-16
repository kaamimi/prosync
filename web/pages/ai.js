/* function genresponse(){
    var userprompt=document.getElementById("aiinput").value;
    let response=eel.askgemini(userprompt);

    var parent = document.querySelector(".content");
    var resp=document.createElement("p");
    resp.textContent = response;
    console.log(response);
    parent.appendChild(resp);
} */
function genresponse() {
    var question = document.getElementById("aiinput").value;
    //document.getElementById("load").classList.add("loader");
    eel.askgemini_form(question)(displayResponse);
}

function displayResponse(response) {
    document.getElementById("response").innerText = response;
}
