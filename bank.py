class AccountHolderDetails:
    def __init__(self, name, address, age):
        self.name = name
        self.address = address
        self.age = age


class MyAccount(AccountHolderDetails):
    def __init__(self, accountNumber, balance):
        self.accountNumber = accountNumber
        self.balance = balance
    
    # Adds the amount onto the account balance
    def deposit(self, amount):
        if amount < 0:
            print("Try again")
        self.balance += amount


    def withdrawal(self, amount):
        if amount < 0:
            print("Try again")
        self.balance -= amount
