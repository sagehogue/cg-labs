let color;
function getColor(e) {
    return document.querySelector('#colorPicker').value;
}

document.querySelector('#submit').addEventListener("click", function() {
    document.body.bgColor = getColor();
    }

);
