# This is an ATM machine


print(25 * '=')
print('Welcome to the Bank ATM!')
print(25 * '=')

options = ['deposit', 'withdraw', 'balance', 'exit']

dic_bank_accounts = {'vasil': {'1230': 2000},
                     'georgi': {'3210': 1000},
                     'ivan': {'0000': 1200},
                     'petur': {'5432': 1000},
                     'samir': {'5431': 11000},
                     'ahmed': {'2432': 12000},
                     'daniel': {'0101': 9000},
                     'dimitar': {'0202': 5000},
                     'teodor': {'1111': 6000},
                     'teodora': {'2222': 7000},
                     }



def deposit(deposit_amount, account_balance):
    account_balance = account_balance + deposit_amount
    return [deposit_amount, account_balance]


def withdraw(withdraw, account_balance):
    account_balance = account_balance - withdraw
    return [withdraw, account_balance]

try:
    name = input('Please Enter you name:\n').lower().strip()
    if name in dic_bank_accounts.keys():
        count = 0
        while count < 3:
            password = input('PLEASE ENTER PIN:\n')
            if name in dic_bank_accounts.keys():
                if password in dic_bank_accounts[name]:

                    account_balance = dic_bank_accounts[name][password]
                    user_choice = input('What would you like to do?\n(Deposit, Withdraw, Balance, Exit)?\n').lower().strip()

                    if user_choice not in options:
                        print('We don\'t have this option.')
                        user_choice = input('What would you like to do?\n').lower().strip()
                    elif user_choice == 'deposit':
                        deposit_amount = float(input('How much would you like to deposit today?\n'))

                        result = deposit(deposit_amount, account_balance)
                        deposit_amount = result[0]
                        account_balance = result[1]
                        print(f'Deposit was lv {deposit_amount:.2f}, current balance is lv {account_balance:.2f}!')
                        break

                    elif user_choice == 'withdraw':
                        withdrawing = float(input('How much would you like to Withdraw today?\n'))
                        if withdrawing > account_balance:
                            print(f'Sorry you don\'t have that much balance.\nYour balance is {account_balance} lv.')
                            user_choice = input('What would you like to do?\n').lower()
                        else:
                            result = withdraw(withdrawing, account_balance)
                            withdraw = result[0]
                            account_balance = result[1]
                            print(f'You have Withdraw {withdraw:.2f}, current balance is lv {account_balance:.2f}')
                            break
                    elif user_choice == 'balance':
                        print(f'Your Balance is {account_balance}!')
                        break
                    elif user_choice == 'exit':
                        print(25 * '=')
                        print('You have Exited the ATM!')
                        print(25 * '=')
                        break
                else:
                    count += 1
                    x = 3 - count
                    print(f'Invalid pin! Please enter correct pin! {x} try\'s left')
                    if count == 3:
                        print(25 * '=')
                        print('Your card has been blocked!')
                        print(25 * '=')

    else:
        print(30 * '=')
        print('This account doesn\'t exists.\nPlease try again.')
        print(30 * '=')

except ValueError:
    print('Invalid input')