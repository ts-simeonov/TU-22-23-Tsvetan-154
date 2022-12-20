# User
class InvalidUserData(Exception):
    def __init__(self, invalid_data, *args):
        message = f'Invalid user data: {invalid_data}'
        super().__init__(message, *args)

class UserNotFound(Exception):
    def __init__(self, message = "User couldn't be found", *args):
        super().__init__(message, *args)

class UserAlreadyExists(Exception):
    def __init__(self, message = "User already exists", *args: object) -> None:
        super().__init__(message, *args)

class UserAlreadyOwnsAccount(Exception):
    def __init__(self, message = "This user already owns this account", *args):
        super().__init__(message, *args)

# Account 
class AccountNotFound(Exception):
    def __init__(self, message = "The account couldn't be found", *args):
        super().__init__(message, *args)

class UnsufficientBalance(Exception):
    def __init__(self, message = "Cannot withdraw this much money; insufficient balance", *args):
        super().__init__(message, *args)

class InvalidAccountData(Exception):
    def __init__(self, invalid_data, *args):
        message = f'Invalid account data: {invalid_data}'
        super().__init__(message, *args)

class InvalidAccountType(Exception):
    def __init__(self, message = "Invalid account type, please enter one of the following: SAVINGS, CREDIT, CHECKING", *args):
        super().__init__(message, *args)

class InvalidCurrency(Exception):
    def __init__(self, message = "Invalid currency, please enter one of the following: BGN, EUR, USD", *args):
        super().__init__(message, *args)

# Bank


# Menu
class InvalidMenuChoice(Exception):
    def __init__(self, message = "Error: Invalid choice", *args):
        super().__init__(message, *args)