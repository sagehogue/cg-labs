// response_list = ['It is certain', 'It is decidedly so', 'Without a doubt',
// 'Yes definitely', 'You may rely on it', 'As I see it, yes',
// 'Most likely', 'Outlook good', 'Yes', 'Signs point to yes',
// 'Reply hazy try again', 'Ask again later', 'Better not tell you now',
// 'Cannot predict now', 'Concentrate and ask again', 'Don’t count on it',
// 'My reply is no', 'My sources say no', 'Outlook not so good']

// print('Hello user!')
// print('')
// query = input('Ask your question of probability.\n>')

// var rand = myArray[Math.floor(Math.random() * myArray.length)];
// print(choice(response_list))

// queryagain = input('Would you like to ask another question? If not, enter "done"\n>')
// query2 = queryagain.lower()
// while query2 != 'done':
//     print(choice(response_list))
//     query2 = input('Would you like to ask another question? If not, enter "done"\n>')

let responseArray = ['It is certain', 'It is decidedly so', 'Without a doubt',
    'Yes, definitely', 'You may rely on it', 'As I see it, yes', 'Most likely',
    'Outlook good', 'Yes', 'Signs point to yes', 'Reply hazy try again', 'Ask again later',
    'Concentrate on your question harder and ask again.', 'Don\'t count on it'];

    while (true === true) {
        let query = prompt('Hello user!\n Ask your question of probability to the magicEightBall!');
        let choice = responseArray[Math.floor(Math.random() * responseArray.length)];
        console.log(`You asked \'${query}\'\nI answer thee \'${choice}\'`);
        let queryDos = prompt('Would you like to ask another question? If so, enter \'yes\'').toLowerCase();
        if (queryDos.indexOf('yes') === -1) {
            break;
        }
    }