def validate_pin(client):
    for _ in range(3):
        pin_input = input('Enter pin code: ')
        if pin_input == client['pin']:
            return True
    else:
        print('Card blocked!')
        return False

def get_withdraw_amount(balance):
    while True:
        try:
            withdraw_amount = float(input('Enter withdraw amount: '))
            if withdraw_amount < 0:
                print('Withdraw amount have to be a positive number (example: 123.45)')
            elif withdraw_amount <= balance:
                return withdraw_amount
            else:
                print(f"You don't have enough money. Your balance is {balance}. Try again.")
        except ValueError:
            print('Withdraw amount have to be a number (example: 123.45)')

def get_deposit_amount():
    while True:
        try:
            deposit_amount = float(input('Enter deposit amount: '))
            if deposit_amount < 0:
                print('Deposit amount have to be a positive number (example: 123.45)')
            else:
                return deposit_amount
        except ValueError:
            print('Deposit amount have to be a number (example: 123.45)')