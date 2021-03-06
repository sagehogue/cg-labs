function newDice(id, integer, sides=6) {
    this.sides = sides;
    this.value = integer;
    this.changeValue = rollSingle(this.id);
    this.id = id;
    this.face =
    document.querySelector('#diceArea').innerHTML += (determineImage(integer, id));
}

//use setAttribute to change id and display - may be easier than doing some other weird shit.
//I think I should do these in the proper order - I am getting too frustrated doing this one and I am not behaving well.

function rollDice() {

    let rollNumber = document.querySelector('#userInput').value;
    let toRoll = parseInt(rollNumber);
let idArray = [0];
    for (let i=0; i < toRoll; i++) {
        let newID = (idArray[idArray.length - 1] + 1);
        idArray.push(newID);
        let int = Math.floor(Math.random() * 6) + 1;
        // document.queryselector('#diceArea').innerHTML.concat(determineImage(int));
        //  document.querySelector('#diceArea').innerHTML += (determineImage(int, newID));
    }
}

function rollSingle(id=null) {
    event.target.innerHTML = "";
    console.log(event.target.id);
    let int = Math.floor(Math.random() * 6) + 1;
    if (id = null) {
        document.querySelector('#diceArea').innerHTML += (determineImage(int));
    } else {
        document.querySelector(`#${id}`).innerHTML = (determineImage(int));
    }
}
function determineImage(face, ID) {
    switch(face) {
        case 1:
            return `<li id="${ID}"><img src="" alt="Value 1"></li>`;
        case 2:
            return `<li id="${ID}"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/34/Dice-2.svg/836px-Dice-2.svg.png" alt="Value 2"></li>`;
        case 3:
            return `<li id="${ID}"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Dice-3.svg/557px-Dice-3.svg.png" alt="Value 3"></li>`;
        case 4:
            return `<li id="${ID}"><img src="https://upload.wikimedia.org/wikipedia/commons/1/16/Dice-4.svg"  alt="Value 4"></li>`;
        case 5:
            return `<li id="${ID}"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/dc/Dice-5.svg/2000px-Dice-5.svg.png"  alt="Value 5"></li>`;
        case 6:
            return `<li id="${ID}"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Dice-6.svg/2000px-Dice-6.svg.png"  alt="Value 6"></li>`;
    }
}


document.querySelector.addEventListener('click', rollDice);
document.querySelector('#diceArea').addEventListener(('click', rollSingle));
