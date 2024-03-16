var pos=1;
var pts=30;
function adduser() {  
    var table = document.getElementById("board");  
    var row = document.createElement("tr");
    var user=document.getElementById("adderinput").value;
    console.log(user);
    
    var position = document.createElement("td");
    position.textContent = pos;
    pos++;
    var username = document.createElement("td");
    username.textContent = user;
    var points = document.createElement("td");
    points.textContent = pts--;
   
    row.appendChild(position);
    row.appendChild(username);
    row.appendChild(points);
    table.appendChild(row);
}