// let userGuessCount = 0;
let userGuessCount = 0;
let computerGuess = Math.floor(Math.random() * 10) + 1;

let playing = true;
let userGuess;
while (computerGuess < 7) {
    userGuess = prompt('What is your guess?');
    userGuessCount++;

    if (userGuess < computerGuess) {
        console.log('You guessed too low!')
    }
}

blaaa