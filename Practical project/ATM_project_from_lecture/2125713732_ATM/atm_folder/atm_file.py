from helpers_folder.helpers_file import validate_pin, get_withdraw_amount, get_deposit_amount


def atm_func(clients):
    client_name_input = input('Enter client name: ')

    if clients.get(client_name_input):
        client = clients[client_name_input]
        if validate_pin(client):
            balance = client['balance']
            print(f'Card balance: {balance}')
            action = input('Enter action (Withdraw/Deposit/Balance): ').lower().replace(' ', '')
            if action == 'withdraw':
                withdraw_amount = get_withdraw_amount(balance)
                new_balance = balance - withdraw_amount
                print(f'You just withdraw {withdraw_amount:.2f}\nYour new balance is {new_balance:.2f}')
            elif action == 'deposit':
                deposit_amount = get_deposit_amount()
                new_balance = balance + deposit_amount
                print(f'You just deposit {deposit_amount:.2f}\nYour new balance is {new_balance:.2f}')
            elif action == 'balance':
                print(f'Card balance: {balance}')
            else:
                print('Invalid action')
    else:
        print('There is no such client')
