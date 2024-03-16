function genresponse(response){
    var userprompt=document.getElementById("aiinput").value;
    eel.askgemini(userprompt);

    var parent = document.querySelector(".content");
    var resp=document.createElement("p");
    resp.textContent = response;
    console.log(response);
    parent.appendChild(resp);
}