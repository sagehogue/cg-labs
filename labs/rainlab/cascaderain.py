# PCC Cascade Weather Lab!
def get_data():
    with open('rain_data.txt', 'r', encoding='utf-8') as f:
        file = f.readlines()
        return file

def rain_diction(rain_data):
    rain_dict = {}
    for i in rain_data:
        i1 = i.strip()
        listofsplitstr = i1.split('  ')
        rain_dict[listofsplitstr[0]] = listofsplitstr[2]
    return rain_dict


def get_max_rain(rain_dict):
    max_rain_val = max(rain_dict.values())
    corresponding_date = (list(rain_dict.keys())[list(rain_dict.values()).index(max_rain_val)])
    return corresponding_date, max_rain_val

rainy_data = get_data()
rain_dictionary = rain_diction(rainy_data)
date, rainval = get_max_rain(rain_dictionary)
print('On {} {} inches of rain were recorded, the most of any day on record.'.format(date, rainval))
