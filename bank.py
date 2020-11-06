class AccountHolderDetails:
    def __init__(self, name, address, age):
        self.name = name
        self.address = address
        self.age = age

    def display(self):
        print(f"Name: {self.name}")
        print(f"Address: {self.address}")
        print(f"Age: {self.age}")


class MyAccount(AccountHolderDetails):
    # The bank fees are set at 5%
    def __init__(self, accountNumber, balance, details):
        self.details = details
        self.accountNumber = accountNumber
        self.balance = balance
        self.bank_fees = 0.05
    
    # Adds the amount onto the account balance
    def deposit(self, amount):
        if amount < 0:
            print("Try again")
        self.balance += amount

    # Subtracts the money from account balance
    # Early withdrawals also incur a bank fee
    def withdrawal(self, amount):
        if amount < 0:
            print("Try again")
        self.balance -= amount + self.bankFees()

    # This method returns 5% of the current account balance
    def bankFees(self):
        return self.balance * self.bank_fees

    # Displays account details
    def display(self):
        self.details.display()
        print(f"\nAccount Number: {self.accountNumber}")
        print(f"Balance: £{self.balance}")        
        print(f"Bank Fees: {self.bank_fees*100} %")        


class ManageAccount(MyAccount):
    def __init__(self, account):
        self.account = account

    def display(self):
        self.account.display()
