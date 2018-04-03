class ATM:

    def __init__(self, n, y=0):
        self.name = n.title()
        self.balance = y
        self.interest_rate = 0.1

    def check_balance(self):
        return '\nYour account balance is ${}\n'.format(self.balance)

    def deposit(self, amount):
        self.balance += amount
        print('\nThank you for your deposit. \n' + self.check_balance())

    def check_withdrawal(self, amount):
        if (self.balance - float(amount)) >= 0:
            return True
        else:
            return False

    def withdraw(self, amount):
        wd_chk = self.check_withdrawal(amount)
        if wd_chk is True:
            self.balance -= float(amount)
            print('\nYour withdrawal has been completed.\n'+ self.check_balance())
        else:
            print('\nThere are not enough funds in your account to complete that transaction.\n' + self.check_balance())

    def calc_interest(self, t):
        accrual = self.balance * ((1 + (((self.interest_rate / 100) / 365)) ** (365 * t)))
        daily_accrual = (accrual / 365)
        print('\n{}. Your annual interest earnings are ${}. Your daily interest earnings are {}.\n'.format(self.check_balance, accrual, daily_accrual))


def user_reg():
    accconf = input('\nDo you have an account already? (y/n)\n: ').lower()
    if accconf in 'n' or accconf in 'no':
        ns_name = input('\nName for the new account?\n: ').capitalize
        new_acc = ATM(ns_name)
        account_list.append(new_acc)
        return new_acc
    elif accconf in 'y' or accconf in 'yes':

        ns_name = input('\nWhat name is your account under? Please enter your full name correctly.\n: ').title()
        for i in account_list:
            print(i.name)
            if ns_name.title() == i.name:
                user_account = i
                return user_account
        else:
            new_acc = ATM(ns_name)
            account_list.append(new_acc)
            print('\nThere was no account under that name, so I have created one for you.\nNew account under {}\n'.format(new_acc.name))
            return new_acc


def menu(user_account):
    q = input('\nWelcome {}! What would you like to do?\n1. Check Balance\n2. Make Deposit\n3. Make Withdrawal\n4. Calculate Interest\n7. Log Out \n 9. Exit\n\n\n: '.format(user_account.name))
    if q in '1':
        print(user_account.check_balance())
    elif q in '2':
        deposit_amt = float(input('How much would you like to deposit?\n: '))
        user_account.deposit(deposit_amt)
    elif q in '3':
        withdraw_amt = float(input('How much would you like to withdraw?\n: '))
        user_account.withdraw(withdraw_amt)
    elif q in '4':
        time = float(input('What length of time (in years) would you like interest calculated for?\n: '))
        user_account.calc_interest(time)
    elif q in '7':
        logged_in = False
    elif q in '9':
        exit()

def onemore():
    while True:
        again = input('\nWould you like to access another account? y/n\n: ').lower()
        if again in 'y' or again in 'yes':
            return
        elif again in 'n' or again in 'no':
            exit()

account_list = []
Sage = ATM('Sage Hogue')
Aaron = ATM('Aaron Holden')
Dominic = ATM('Dominic Perreira')
account_list.append(Sage)
account_list.append(Aaron)
account_list.append(Dominic)
atm_on = True
while atm_on == True:
    user_acc = user_reg()
    logged_in = True
    while logged_in == True:
        menu(user_acc)

