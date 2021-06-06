from atm_folder.atm_file import atm_func

CLIENTS = {
    'Pesho': {
        'pin': '1234',
        'balance': 1000.00
    },
    'Gosho': {
        'pin': '1234',
        'balance': 1000.00
    }
}

if __name__ == '__main__':
    atm_func(CLIENTS)
