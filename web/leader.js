function adduser(pos,user,pts) {    
    var newRow = document.createElement("tr");
    
    var position = document.createElement("td");
    position.textContent = pos;
    var username = document.createElement("td");
    username.textContent = user;
    var points = document.createElement("td");
    points.textContent = pts;
   
    newRow.appendChild(position.textContent);
    newRow.appendChild(username.textContent);
    newRow.appendChild(points.textContent);
}