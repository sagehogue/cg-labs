// g_num = int(input('Please type your numerical grade\n: '))
let score = prompt('Please enter your numerical grade:');

// plus_minus = ""
let plusMinus;
// if (g_num % 10) >= 7:
if ((score % 10) >= 7 || score == 100) {
//     plus_minus = "+"
    plusMinus = '+ ';
// elif (g_num % 10) <= 3:
//     plus_minus = "-"
} else if ((score % 10) <= 3) {
    plusMinus = '- ';
} else {
    plusMinus = ' ';
}
// if g_num > 89:
//     print('You got an A' + plus_minus + "!")
if (score > 89) {
    console.log(`You got an A${plusMinus}Congratulations! You're amazing.`);
// elif g_num >= 80:
//     print('You got a B' + plus_minus + "!")
} else if (score >= 80) {
    console.log(`You got a B${plusMinus}Congratulations! That's a pretty solid score!`);
// elif g_num >= 70:
//     print('You got a C' + plus_minus + "!")
} else if (score >= 70) {
    console.log(`You got a C${plusMinus}Congratulations! You did acceptably.`);
// elif g_num >= 60:
//     print('You got a D' + plus_minus + "!")
} else if (score >= 60) {
    console.log(`You got a D${plusMinus}Congratulations! You actually managed to pass this one!`);
// elif g_num >= 50:
//     print('You got a F' + plus_minus + "!")
} else if (score <= 59) {
    console.log('You failed son. There are no winners here. F.');
} else {
    console.log('What are you doing with your life?');
}
// else:
//     print('You incorrectly input your grade or you got a terrible one.')
