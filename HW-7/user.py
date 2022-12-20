from errors import UserAlreadyOwnsAccount, AccountNotFound
# from pprint import pprint

class User:
    def __init__(self, names, egn) -> None:
        self.names = names
        self.egn = egn
        self.accounts = []

    def get_print(self):
        return f"User({self.names}, {self.egn}, accounts: [{len(self.accounts)}])"

    def add_account(self, account):
        if account in self.accounts:
            raise UserAlreadyOwnsAccount("Error: This account already belongs to this user")
            
        self.accounts.append(account)

    def get_accounts(self):
        print(f'The user currently has these accounts: {self.accounts}')

    def find_acc(self, curr, typee):
        for i in self.accounts:
            if i.currency == curr and i.typee == typee:
                return i
    
    def deposit_money(self, curr, typee, amount):
        acc = self.find_acc(curr, typee)
        if acc == None:
            raise AccountNotFound()
        acc.deposit(amount)
        print(f'Current balance: {acc.balance}')

    def withdraw_money(self, curr, typee, amount):
        acc = self.find_acc(curr, typee)
        if acc == None:
            raise AccountNotFound()
        acc.withdraw(amount)
        print(f'Current balance: {acc.balance}')