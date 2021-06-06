__all__ = ['deposit', 'withdraw']

def deposit(deposit_amount, account_balance):
    account_balance = account_balance + deposit_amount
    return [deposit_amount, account_balance]


def withdraw(withdraw, account_balance):
    account_balance = account_balance - withdraw
    return [withdraw, account_balance]