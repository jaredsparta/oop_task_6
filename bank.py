import random

# This holds the user's name, address and age
class AccountHolderDetails:
    def __init__(self, name, address, age):
        self.name = name
        self.address = address
        self.age = age


    def display(self):
        print(f"Name: {self.name}")
        print(f"Address: {self.address}")
        print(f"Age: {self.age}")

# Holds accountnumber as a private variable, balance and bank fees
class MyAccount(AccountHolderDetails):
    # The bank fees are set at 5%
    def __init__(self, balance, details):
        self.details = details
        self.balance = balance
        self.bank_fees = 0.05
        self.__accountNumber = self.__create_account_number()

    @property
    def accountNumber(self):
        return self.__accountNumber

    # This should be private so no account number can be remade
    def __create_account_number(self):
        number = ""
        while len(number) < 8:
            number += str(random.choice(range(1,10)))
        return number


    # Adds the amount onto the account balance
    def deposit(self, amount):
        if amount < 0:
            print("\nTry again")
        self.balance += amount

    # Subtracts the money from account balance
    # Early withdrawals also incur a bank fee
    def withdrawal(self, amount):
        if amount < 0:
            print("\nTry again")
        self.balance -= amount + self.bankFees()

    # This method returns 5% of the current account balance
    def bankFees(self):
        return self.balance * self.bank_fees

    # Displays account details
    def display(self):
        print("")
        print("="*30)
        print(f"Account Number: {self.accountNumber}")
        print(f"Balance: £ {self.balance}")        
        print(f"Bank Fees: {self.bank_fees*100} %")        
        print("="*30)

# This class acts like a bank machine
# Allows one to view balance, withdraw, deposit
class ManageAccount(MyAccount):
    def __init__(self, account):
        self.account = account
        self.options()
        print("\nThanks for using this machine!")

    
    def options(self):
        while True:
            print("="*20)
            print("""\nWhat would you like to do?
                    1. Check balance
                    2. Withdraw money
                    3. Deposit money
                    4. Exit""")
            choice = input("--> ")
            
            # Submenu for option 1 (check balance)
            if choice == "1":
                self.account.display()
                subchoice = self.option1_choice()
                if subchoice == "Y":
                    continue
                break
            
            # Submenu for option 2 (withdrawal)
            if choice == "2":
                subchoice = self.withdrawal_manage()
                if subchoice == "Y":
                    continue
                break

            # Submenu for option 3 (deposit)
            if choice == "3":
                subchoice = self.deposit_manage()
                if subchoice == "Y":
                    continue
                break

            if choice == "4":
                break

    # Returns whether or not to continue after option 1
    def option1_choice(self):
        print("\nWould you like to do anything else? (Y/N)")
        while True: 
            choice = input("-->  ").upper().strip()
            if choice in ["Y", "N"]:
                return choice
            continue
    
    # Returns whether or not to continue after option 2
    def withdrawal_manage(self):
        print("\nThis machine only has £10 and £20 notes")
        print("How much would you like to withdraw?")
        while True:
            try:
                money = int(input("-->  "))
                if money > self.account.balance:
                    print("\nInsufficient funds")
                    break
                if money % 10 == 0:
                    self.account.withdrawal(money)
                    print(f"\nYou have withdrawn £ {money}")
                    print(f"Your new balance is £ {self.account.balance}")
                    break
                print("This machine only has £10 and £20 notes")
            except:
                continue

        print("")
        print("="*42)    
        print("Would you like to do anything else? (Y/N)")
        print("="*42)

        while True:
            subchoice = input("-->  ").upper()
            if subchoice in ("Y", "N"):
                return subchoice
            continue

    # Returns whether or not to continue after option 3
    def deposit_manage(self):
        print("\nHow much would you like to deposit?")
        # It will ask for the amount of money to deposit
        # This while loop will only allow valid money values
        while True:
            try:
                money = float(input("-->  "))
                self.account.deposit(money)
                print(f"\nYou have deposited £ {money}")
                print(f"Your new balance is £ {self.account.balance}")
                break
            except:
                continue
        print("")
        print("="*42)
        print("Would you like to do anything else? (Y/N)")
        print("="*42)

        while True:
            subchoice = input("-->  ").upper()
            if subchoice in ("Y", "N"):
                return subchoice
            continue

# Initialises an account holder
if __name__ == "__main__":
    User = AccountHolderDetails("Person", "1st Street", 21)
    User_account = MyAccount(1000, User)
    manage = ManageAccount(User_account)
