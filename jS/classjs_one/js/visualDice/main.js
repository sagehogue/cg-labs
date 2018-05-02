function Die(id, sides = 6) {
    this.sides = sides;
    this.value = Math.floor(Math.random() * this.sides) + 1;
    this.id = id;
    this.display = function () {
        let liID = "li" + this.id;
        return `<li id="${liID}"><img src="${this.value}.svg" id="${this.id}" class="castDie" alt="${this.value}>"</li>`;
    }
}

function roleSingle() {
    console.log(event.target);
    let subject = $(event.target);
    // event trigger - the image
    // id of parent list item for deletion
    let liID = subject.id;
    console.log($('#diceSum').text());
    let curSum = parseInt($('#diceSum').text());
    let toRemove = parseInt(event.target.alt);
    console.log(event.target.alt);

    let newSum;
    let targetForDestruction = event.target.parentNode;
    if (targetForDestruction.nodeName !== 'DIV' && targetForDestruction.nodeName !== 'UL') {
        curSum -= toRemove;
        let newDie = new Die(liID);
        newSum = curSum + newDie.value;
        let sumLocation = $('#diceSum');
        sumLocation.empty();
        sumLocation.text(newSum);
        // liTarget = $(`#diceArea:eq(${liPosition}+1)`);
        $(targetForDestruction).after(newDie.display());
        $(targetForDestruction).remove();
    }
}

function rollAll() {
    let ourUL = $('#diceArea');
    ourUL.html('');
    let rollNumber = parseInt(document.querySelector('#userInput').value);
    let idArray = [0];
    let diceSum = 0;
    for (i = 0; i < rollNumber; i++) {
        let curID = (idArray.length);
        idArray.push(curID);
        let diceObj = new Die(curID);
        let curDisplay = diceObj.display();
        ourUL.append(curDisplay);
        diceSum += diceObj.value;
    }
    $('#diceSum').text(diceSum);
}

$('#rollButton').click(rollAll);
$('#diceArea').click(roleSingle);