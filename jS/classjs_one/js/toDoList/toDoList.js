// Let’s make a simple todo-list which supports the following operations:
//
// add an item to the list
// remove an item from the list
// mark an item as completed
// Removed items should disappear entirely. Completed items should appear at the bottom (or in a separate list) with a line through them.

function addTask(identifier) {
    let content = document.querySelector('#newItem').value;
    // let newBox = document.createElement('input');
    // newBox.setAttribute("type", "checkbox");
    // newBox.setAttribute("id", `${identifier}box`);
    // newBox.setAttribute("class", "chk");
    document.querySelector('#taskList').innerHTML += `<li id=${identifier}><input type="checkbox" id=${identifier}box class="chk"><label class="checkBox" for=${identifier}box>${content}</label></li>';
}

function removeTask(){

}

function getID() {

}

function markComplete() {

}

function addTask(e) {
let newTaskVal = document.querySelector('#newItem').value;
let newTask = document.createElement('li');
let taskID = (document.querySelector('#taskList').children.length) + 1;
let ulID = (document.querySelector('#taskList').children.length) + 100;
let newLabel = document.createElement('label');
newLabel.setAttribute('for', ulID);
newLabel.appendChild(document.createTextNode(newTaskVal));


newTask.appendChild(newLabel);
newTask.appendChild(newBox);
newTask.setAttribute("id", taskID);
document.querySelector('#taskList').appendChild(newTask);
document.querySelector('input #ulID').addEventListener("change", isDone());
}