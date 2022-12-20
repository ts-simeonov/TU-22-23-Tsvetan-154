from errors import InvalidAccountType, InvalidCurrency, InvalidAccountData, UnsufficientBalance

class Account:
    ACC_TYPES = ("SAVINGS", "CREDIT", "CHECKING")
    CURRENCIES = ('BGN', 'EUR', 'USD')

    def __init__(self, iban, currency, typee) -> None:
        if typee not in Account.ACC_TYPES:
            raise InvalidAccountType()
        if currency not in Account.CURRENCIES:
            raise InvalidCurrency()
        if len(iban) != 16:
            raise InvalidAccountData('Invalid IBAN')
        self.iban = iban
        self.currency = currency
        self.typee = typee
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        a = self.balance
        a -= amount
        if a < 0:
            raise UnsufficientBalance()
        else:
            self.balance -= amount