#wow I actually finished it

import requests

def get_location():
    return input('For what city do you need a report?.\n: ')

def get_fc_choice():
    return input('celsius or fahrenheit?\n: ')

def get_dtval():
    return input('What is the date for which you want a weather report? (yyyy-mm-dd)\n: ')

def connect(cityname):
    package = {
    'APPID': '4c4fabbb07ec7207d949ecf21172ab8b',
    'units': 'imperial',
    'q': '{}'.format(cityname)
    }
    return requests.post('http://api.openweathermap.org/data/2.5/forecast', params=package)

location = get_location()
info_dict = connect(location).json()
temp_choice = get_fc_choice()
usable_temp = info_dict['list'][1]['main']['temp']
if temp_choice.lower() in 'c' or temp_choice.lower() in 'celsius':
    usable_temp = float(usable_temp)
    usable_temp = ((usable_temp - 32) * 5/9)
    print('The temperature in {} is {} degrees celsius.'.format(location, usable_temp))
else:
    print('The temperature in {} is {} degrees fahrenheit.'.format(location, usable_temp))
