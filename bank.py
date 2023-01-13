from models.checking_account import CheckingAccont
from typing import List
from time import sleep

checking_accounts: List[CheckingAccont] = []

def main():
    menu()

def menu():
    print("Welcome to the Kelvin's Bank!")
    print('1 - Open an account')
    print('2 - Withdraw cash')
    print('3 - Deposit cash')
    print('4 - Transfer cash')
    print('5 - List of accounts')
    print('6 - Close the system')

    operation = int(input('Please choose your operation: '))

    try:
        if operation == 1:
            open_an_account()
        elif operation == 2:
            withdraw_cash()
        elif operation == 3:
            deposit_cash()
        elif operation == 4:
            transfer_cash()
        elif operation == 5:
            list_accounts()
        elif operation == 6:
            print('You close the system. See you soon!')
            exit()
        else:
            print('Choose a valid operation to continue')
            sleep(1)
            menu()
    except ValueError:
        print('Choose a valid operation to continue')
        menu()


def open_an_account() -> None:
    print("Let's open a new account!")
    print('-------------------------')

    name = input("What's the name of the holder? ")
    balance = float(input('How much is the initial deposit? '))

    if len(checking_accounts) > 0:
        for account in checking_accounts:
            if name == account.holder_name:
                print('This client has an account already.')
                sleep(2)
                menu()
        count = CheckingAccont(name, balance)
        checking_accounts.append(count)
        print('Congratulations! You opened a new account.')
        sleep(2)
        menu()
    else:
        count = CheckingAccont(name, balance)
        checking_accounts.append(count)
        print('Congratulations! You opened a new account.')
        sleep(2)
        menu()

def withdraw_cash():
    if len(checking_accounts) > 0:
        print('You chose the withdraw option.')
        account_number: int = int(input("What's the number of the account to do the withdraw? "))
        value: float = float(input('How much do you want to withdraw? '))

        account: CheckingAccont = get_account_by_number(account_number)

        if value <= account.balance:
            new_balance = account.balance - value
            account.balance = new_balance
            print(f'You made the withdraw in the value ${value:.2f}. The balance of the {account.holder_name} account is'
                  f' now ${account.balance:.2f}')
            sleep(2)
            menu()
        else:
            print('Insufficient funds!')
            sleep(2)
            menu()
    else:
        print("There's no checking account registered.")
        sleep(2)
        menu()


def deposit_cash():
    if len(checking_accounts) > 0:
        print('You chose the deposit option.')
        account_number: int = int(input("What's the number of the account to do the deposit? "))
        value: float = float(input('How much do you want to deposit? '))

        account: CheckingAccont = get_account_by_number(account_number)

        if value > 0:
            new_balance = account.balance + value
            account.balance = new_balance
            print(f'You made the deposit in the value ${value:.2f}. The balance of the {account.holder_name} account is'
                  f' now ${account.balance:.2f}')
            sleep(2)
            menu()
        else:
            print('You cannot deposit a negative or neutral value!')
            sleep(2)
            menu()
    else:
        print("There's no checking account registered.")
        sleep(2)
        menu()

def transfer_cash():
    if len(checking_accounts) > 1:
        original_account_number: int = int(input("What's the number of the account that will transfer the money? "))
        destination_account_number: int = int(input("What's the number of the account that will receive the money? "))
        value: float = float(input('How much do you want to transfer? '))

        original_account = get_account_by_number(original_account_number)
        destination_account = get_account_by_number(destination_account_number)

        if value <= original_account.balance:
            new_balance_original_account = original_account.balance - value
            new_balance_destination_account = destination_account.balance + value

            original_account.balance = new_balance_original_account
            destination_account.balance = new_balance_destination_account

            print(f'The transfer of $ {value:.2f} was successful!')
            print(f'The balance of the {original_account.holder_name} account is now ${original_account.balance:.2f}')
            print(f'The balance of the {destination_account.holder_name} account is now ${destination_account.balance:.2f}')
            sleep(2)
            menu()
        else:
            print('Insufficient funds!')
            sleep(2)
            menu()
    else:
        print("You need at least 2 accounts registered to do a transfer.")
        sleep(2)
        menu()

def list_accounts():
    if len(checking_accounts) > 0:
        print('List of accounts:')
        for account in checking_accounts:
            print(account)
            print('-----------------')
            sleep(1)
    else:
        print("There's no account registered.")
    sleep(2)
    menu()

def get_account_by_number(number: int) -> CheckingAccont:
    if len(checking_accounts) > 0:
        print('List of accounts:')
        print('-----------------')
        for account in checking_accounts:
            if number == account.account_number:
                return account
        print("That checking account was not found.")
        sleep(2)
        menu()
    else:
        print("There's no checking account registered.")
        sleep(2)
        menu()

if __name__ == '__main__':
    main()