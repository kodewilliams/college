class BankAccount:
    def __init__ (self, checking, savings):
        self.checking_amount = checking
        self.savings_amount = savings
        self.printDetails()

    def deposit_into_checking(self, amount):
        self.checking_amount += amount
        self.printDetails()

    def deposit_into_savings(self, amount):
        self.savings_amount += amount
        self.printDetails()

    def withdraw(self, amount):
        if self.checking_amount >= amount:
            self.checking_amount -= amount
        elif self.checking_amount >= 0 and amount > self.checking_amount:
            balance = amount - self.checking_amount
            self.checking_amount  = 0
            self.savings_amount -= balance
        self.printDetails()

    def printDetails(self):
        print ('Checking account balance: $' + str(self.checking_amount))
        print ('Savings account balance: $' + str(self.savings_amount))
        print ()



my_account = BankAccount(20, 50)
my_account.deposit_into_checking(20)
my_account.deposit_into_savings(10)
my_account.withdraw(80)
my_account.withdraw(50)
        
