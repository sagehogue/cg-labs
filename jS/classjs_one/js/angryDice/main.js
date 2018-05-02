function isSix() {
    let radioButton = event.target;
    console.log(radioButton);
    console.log(radioButton.id);
    if (radioButton.id === "firstRadio") {
        let alt = $('#firstDisplay > img').attr("alt");
        if (alt = "6") {
            radioButton.checked = false;
            alert("You cannot hold a six! Don't even try!")
        }
    } else if (radioButton.id === "secondRadio") {
        let alt = $('#secondDisplay > img').attr("alt");
        if (alt = "6") {
            radioButton.checked = false;
            alert("You cannot hold a six! Don't even try!")
        }
    }
}

function angryDice() {
    console.log('Angry Dice!');
    $('#displayBoard > p').text(`Grr, you got angry dice!!!`);
    $('#roundCount').text('1')
//    this would be a lovely place to put some angry animations.
}

// function isChecked() {
//     if (radioButton.checked === true) {
//         radioButton.checked = false;
//     }
// }

function clearHolds() {
    $('#firstRadio').prop("checked", false);
    $('#secondRadio').prop("checked", false);
}

function determineCurrentRound() {
    return parseInt($('#roundCount').text());
}

function checkRoundWin(firstVal, secondVal, currentRound) {
    console.log('Check the round!');
    switch (currentRound) {
        case 1:
            return (firstVal === 1 && secondVal === 2 || firstVal === 2 && secondVal === 1);
        case 2:
            return firstVal === 3 && secondVal === 4 || firstVal === 4 && secondVal === 3;
        case 3:
            return firstVal === 5 && secondVal === 6 || firstVal === 6 && secondVal === 5;
    }
}

function rollAll() {
    let round = determineCurrentRound();
    console.log(`Round ${round}`);
    // console.log($('#firstRadio').is(':checked'));
    if ($('#firstRadio').is(':checked') === false) {
        $('#firstDisplay').empty();
        let firstNewNum = Math.floor(Math.random() * 6) + 1;
        $('#firstDisplay').html(`<img src="img/${firstNewNum}.png" class="diceImage" alt="${firstNewNum}">`);
        // } else if (parseInt($('#firstDisplay > img').attr('alt')) === 6) {
        // }
        if ($('#secondRadio').is(':checked') === false) {
            $('#secondDisplay').empty();
            let secondNewNum = Math.floor(Math.random() * 6) + 1;
            $('#secondDisplay').html(`<img src="img/${secondNewNum}.png" class="diceImage" alt="${secondNewNum}">`);
        }
        let firstNum = parseInt($('#firstDisplay img:first').attr("alt"));
        console.log(firstNum);
        // Both return NaN
        let secondNum = parseInt($('#secondDisplay img:first').attr("alt"));
        console.log(secondNum);
        if (firstNum === 3 && secondNum === 3) {
            angryDice();
        } else {
            if (checkRoundWin(firstNum, secondNum, round) === true) {
                round++;
                if (round < 4) {
                    $('#roundCount').text(round);
                    $('#firstRadio').attr("checked", false);
                    $('#secondRadio').attr("checked", false);
                } else {
                    $('#displayBoard > span').remove();
                    $('#displayBoard > h3').text('WINNER! whoop whoop')
                }
            }

        }
        // for (i in $('.diceDisplay')) {
        //     let newHTML;
        //
        //     i.innerHTML.appendChild(newHTML)


//     ourUL = $('#diceArea');
//     ourUL.html('');
//     let rollNumber = parseInt(document.querySelector('#userInput').value);
//     let idArray = [0];
//     let diceSum = 0;
//     for (i = 0; i < rollNumber; i++) {
//         let curID = (idArray.length);
//         idArray.push(curID);
//         let diceObj = new Die(curID);
//         let curDisplay = diceObj.display();
//         ourUL.append(curDisplay);
//         diceSum += diceObj.value;
//     }
//     $('#diceSum').text(diceSum);
    }
}

//
//
$('#buttonRoll').click(rollAll);
$('#buttonHoldClear').click(clearHolds);
$('input').click(isSix);
// $('input').click(isChecked);