#advanced


def get_change():
    while True:
        change = input('How much change do you need?\n: ')
        return change

def make_dollars(total_change):
    dollars = total_change // 100
    extra = total_change % 100
    return dollars, extra

def make_quarters(balanced_change):
    quarters = balanced_change // 25
    extra = balanced_change % 25
    return quarters, extra

def make_dimes(balanced_change):
    dimes = balanced_change // 10
    extra = balanced_change % 10
    return dimes, extra

def make_nickels(balanced_change):
    nickels = balanced_change // 5
    extra = balanced_change % 5
    return nickels, extra

def balance_change(change, madechange):
    out_change = change - madechange

def display_change_array(total_change, dollars, quarters, dimes, nickels, pennies):
    print(str(total_change))
    print('--------------')
    print(str(dollars) + ' dollars')
    print(str(quarters) + ' quarters')
    print(str(dimes) + ' dimes')
    print(str(nickels) + ' nickels')
    print(str(pennies) + ' pennies')


total_change = int(get_change())
dollars, rem_change = make_dollars(total_change)
quarters, rem_change = make_quarters(rem_change)
dimes, rem_change = make_dimes(rem_change)
nickels, rem_change = make_nickels(rem_change)
pennies = rem_change
display_change_array(total_change, dollars, quarters, dimes, nickels, pennies)
