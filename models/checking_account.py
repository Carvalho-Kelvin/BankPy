class CheckingAccont:
    counter: int = 1
    def __init__(self, holder_name: str, balance:float=0) -> None:
        self._account_number: int = CheckingAccont.counter
        self._holder_name: str = holder_name
        self._balance: float = balance
        CheckingAccont.counter += 1


    @property
    def account_number(self) -> int:
        return self._account_number

    @property
    def holder_name(self) -> str:
        return self._holder_name

    @property
    def balance(self) -> float:
        return self._balance

    def __str__(self) -> str:
        return f'Account Number: {self.account_number} \nHolder Name: {self.holder_name} \nBalance: {self.balance}'

    @balance.setter
    def balance(self, new_balance: float):
        self._balance = new_balance




