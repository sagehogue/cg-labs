let time = prompt("What time is it? (HH:AM/PM)");
// console.log(time);
let timeSplit = time.split(":");
// console.log(timeSplit);
let hour = parseInt(timeSplit[0]);
// console.log(hour);
let meridian = timeSplit[1].toLowerCase();
// console.log(meridian);

if ([7, 8, 9].indexOf(hour) > -1) {
    if (meridian ==='am') {
        console.log("It's breakfast!")
    }
    else {
        console.log("It's dinner!")
    }
} else if ([12, 1, 2].indexOf(hour) > -1 && meridian === 'pm') {
    console.log("It's lunchtime!")
} else if (hour >= 10 && hour < 12 && meridian === 'pm' || (hour === 12 || [1, 2, 3, 4].indexOf(hour) > -1) && meridian === 'am') {
    console.log("It's hammerTime!")
}