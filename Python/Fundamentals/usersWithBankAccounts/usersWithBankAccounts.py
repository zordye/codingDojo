class BankAccount:

    def __init__(self, intRate, balance): 
        self.intRate = intRate
        if balance != 0:
            self.balance = balance
        else:
            self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient Funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount

    def displayAccountInfo(self):
        print(f"Balance: {self.balance}")

    def yieldInterest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.intRate)


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(intRate=0.02, balance=0)
    
    def makeDeposit(self, amount):
        self.account.deposit(amount)

    def makeWithdrawal(self, amount):
        self.account.withdraw(amount)

    def displayUserBalance(self):
        self.account.displayAccountInfo()