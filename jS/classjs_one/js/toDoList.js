
// add an item to the list
// remove an item from the list
// mark an item as completed
// Removed items should disappear entirely. Completed items should appear at the bottom (or in a separate list) with a line through them.
function addTask(e) {
let newTaskVal = document.querySelector('#newItem').value;
let newTask = document.createElement('li');
let taskID = (document.querySelector('#taskList').children.length) + 1;
let ulID = (document.querySelector('#taskList').children.length) + 100;
let newLabel = document.createElement('label');
newLabel.setAttribute('for', ulID);
newLabel.appendChild(document.createTextNode(newTaskVal));
let newBox = document.createElement('input');
newBox.setAttribute("type", "checkbox");
newBox.setAttribute("id", ulID);
newBox.setAttribute("class", "chk");
newTask.appendChild(newLabel);
newTask.appendChild(newBox);
newTask.setAttribute("id", taskID);
document.querySelector('#taskList').appendChild(newTask);
document.querySelector('input #ulID').addEventListener("change", isDone());
}
function isDone(selector) {
    if (document.querySelector(selector.id).style.textDecoration = "") {
        document.querySelector(selector.id).style.textDecoration = "line-through";
    } else {
        document.querySelector(selector.id).style.textDecoration = "";
    }
}
document.querySelector('#enter').addEventListener("click", addTask);

