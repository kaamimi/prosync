var n = 0;

function newtask() {
  var taskInput = document.getElementById("task");
  var taskText = taskInput.value.trim();
  
  if (taskText !== "") {
    var List = document.getElementById("list");
    var newTask = document.createElement("li");
    newTask.innerHTML = `
      <div class="task">
        <input type="checkbox" onclick="toggleTask(this)">
        <p>${taskText}</p>
        <button class="delete" onclick="deleteTask(this)">delete</button>
      </div>
    `;
    List.appendChild(newTask);
    n++; 
    taskInput.value = "";
  }
}

function deleteTask(element) {
  var taskItem = element.parentElement;
  taskItem.remove();
  n--; 
}

function toggleTask(element) {
  var values= element.nextElementSibling;
  if (element.checked) {
    values.style.textDecoration = "line-through";
  } else {
    values.style.textDecoration = "none";
  }
}

function clearall(){
  var List = document.getElementById("list");
  List.innerHTML = ""; 
  n = 0; 
}