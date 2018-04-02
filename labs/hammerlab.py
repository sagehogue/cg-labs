#hammerlablabhammer
given_time = input('What time is it? Round to nearest hour in format "12 AM" \n>')
split_time = given_time.split()
ampm = split_time[1].lower()
if int(split_time[0]) in list(range(7, 10)) and ampm == "am":
    print('Breakfast time!')
elif ampm == "pm" and int(split_time[0]) <=2 or int(split_time[0]) == 10:
    print('Lunch time!')
elif int(split_time[0]) in list(range(7, 10)) and ampm == "pm":
    print('Dinner time!')
elif ampm == "pm" and int(split_time[0]) <=2 or int(split_time[0]) == 10:
    print('Lunch time!')
elif (int(split_time[0]) in list(range(10, 12)) and ampm == "pm") or ((int(split_time[0]) in list(range(1, 5)) or int(split_time[0]) == 12) and ampm == "am"):
    print('Hammertime!!')
else:
    print("It's not time.")
# i have created something monstrous and awful
# I realized this was a terrible way to solve this problem around line 9 but soldiered through.
