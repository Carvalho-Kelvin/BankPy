from models.checking_account import CheckingAccont

checking_accounts = []
kelvin_account = CheckingAccont('Kelvin')
mariane_account = CheckingAccont('Mariane', 4500.45)

checking_accounts.append(kelvin_account)


def get_account_by_number(number: int) -> CheckingAccont:
    if len(checking_accounts) > 0:
        for account in checking_accounts:
            if number == account.account_number:
                return account
        print("That checking account was not found.")
        # sleep(2)
        # menu()
    else:
        print("There's no checking account registered.")
        # sleep(2)
        # menu()

print(get_account_by_number(2))