#conversionlab


def get_value():
    while True:
        o_v = int(input('What is the value of the unit you want converted?\n: '))
        return o_v

def get_unit():
    while True:
        o_u = input('What is the unit you wish to convert? (mi, km, ft, m)\n: ').lower()
        if o_u not in ['mi', 'km', 'ft', 'm']:
            print("What's this nonsense?")
            print('')
        else:
            return o_u
def get_target(o_u):
    while True:
        o_t = input('What is the unit you wish to convert to? (mi, km, ft, m)\n: ').lower()
        if o_t not in ['mi', 'km', 'ft', 'm'] or o_t == o_u:
            print("What's this nonsense?")
            print('')
        else:
            return o_t


def display_results(start_val, start_unit, end_val, end_unit):
    return '{}{} converts to {}{}'.format(start_val, start_unit, end_val, end_unit)

# def validate():
#     o_v = get_value()
#     o_u = get_unit()
#     o_t = get_target()
#     while o_u == o_t:
#         print('Do you really need me for that?')
#         print('')
#         o_v = get_value()
#         o_u = get_unit()
#         o_t = get_target()
#     while o_u or o_t not in unit_list:
#         print("What's this nonsense?")
#         print('')
#         o_v = get_value()
#         o_u = get_unit()
#         o_t = get_target()

def convert():
    if o_u == 'ft':
        if o_t == 'mi':
            result_val = (o_v * 0.000189394)
            return result_val
        elif o_t == 'km':
            result_val = (o_v * 0.0003048)
            return result_val
        elif o_t == 'm':
            result_val = (o_v * 0.3048)
            return result_val
    elif o_u == 'mi':
        if o_t == 'km':
            result_val = (o_v * 1.61)
            return result_val
        elif o_t == 'ft':
            result_val = (o_v * 5280)
            return result_val
        elif o_t == 'm':
            result_val = (o_v * 1609.34)
            return result_val
    elif o_u == 'km':
        if o_t == 'mi':
            result_val = (o_v * 0.621371)
            return result_val
        elif o_t == 'ft':
            result_val = (o_v * 3280.84)
            return result_val
        elif o_t == 'm':
            result_val = (o_v * 1000)
            return result_val
    elif o_u == 'm':
        if o_t == 'mi':
            result_val = (o_v * 0.000621371)
            return result_val
        elif o_t == 'km':
            result_val = (o_v * 0.001)
            return result_val
        elif o_t == 'ft':
            result_val = (o_v * 3.28084)
            return result_val

unit_list = ['mi', 'km', 'ft', 'm']

o_v = get_value()
o_u = get_unit()
o_t = get_target(o_u)
result_val = convert()
print(display_results(o_v, o_u, result_val, o_t))
