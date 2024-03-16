var pos=1;

function adduser(user,pts) {  
    var table = document.getElementById("board");  
    var row = document.createElement("tr");
    
    var position = document.createElement("td");
    position.textContent = pos;
    pos++;
    var username = document.createElement("td");
    username.textContent = user;
    var points = document.createElement("td");
    points.textContent = pts;
   
    row.appendChild(position);
    row.appendChild(username);
    row.appendChild(points);
    table.appendChild(row);
}