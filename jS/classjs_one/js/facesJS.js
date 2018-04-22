// from random import choice
// eyes_list = [ ';', '=', '8', '>:', 'x', 'X']
let eyesArray = [ ';', '=', '8', '>:', 'x', 'X'];
// nose_list = ['^', '-', ':']
let noseArray = ['^', '-', ':'];
// mouth_list = ['D', 'd', 'P', 'p', '*', 'O', ']', '[', ')', '(', '#', '@']
let mouthArray = ['D', 'd', 'P', 'p', '*', 'O', ']', '[', ')', '(', '#', '@'];
// i = 1
let counter = 1
while (counter < 11) {
    let selectedEyes = eyesArray[Math.floor(Math.random() * eyesArray.length)];
    let selectedNose = noseArray[Math.floor(Math.random() * noseArray.length)];
    let selectedMouth = mouthArray[Math.floor(Math.random() * mouthArray.length)];
    console.log(`${selectedEyes}${selectedNose}${selectedMouth}`);
    counter++;
}
//     s_eyes = choice(eyes_list)
//     s_nose = choice(nose_list)
//     s_mouth = choice(mouth_list)
//     print("{}{}{}".format(s_eyes, s_nose, s_mouth))
//     i = i + 1
