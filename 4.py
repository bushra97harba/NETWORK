class BankAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0
    def deposit(self, amount):
        self.balance += amount
        print("Deposited: {0:.2f}$".format(amount))
        print("Current balance: {0:.2f}$".format(self.balance))
    def withdrew(self, amount):
        if amount > self.balance:
            print("insufficient balance!")
        else:
            self.balance -= amount
            print("Withdrew:{0:.2f} $".format(amount))
            print(f"Current balance:{0:.2f} $".format(self.balance))
    def get_balance(self):
        return self.balance
    def __str__(self):
        return "account holder:" + self.account_holder+ " balance: " +str(self.balance)

class SavingAccount(BankAccount):
    def __init__(self, account_number, account_holder, interest_rate):
        super().__init__(account_number, account_holder)
        self.interest_rate = interest_rate
    def apply_interest(self):
        interest = self.balance * (self.interest_rate / 100)
        self.balance += interest
        print("Interest applied: {0:.2f}$".format(interest))
        print(f"New balance: {0:.2f}$".format(self.balance))
    def __str__(self):
        return f"account holder: {self.account_holder}, balance: ${self.balance:.2f}, interest rate: {self.interest_rate}%"

account = BankAccount("2574", "bushra")
account.deposit(1000)
account.withdrew(500)
print(account)
saving = SavingAccount("2574", "bushra", 20)
saving.deposit(1000)
saving.apply_interest()
print(saving)
