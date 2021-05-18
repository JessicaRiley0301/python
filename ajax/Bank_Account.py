class BankAccount:
    bank_name = "Rich Bank"
    all_accounts = []
    def __init__(self, int_rate = 0.2, balance = 0): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if BankAccount.can_withdraw(self.balance, amount):
            self.balance -= amount
        else: 
            self.balance = self.balance - 5
            print("Insufficeint funds.")
    def display_account_info(self):
        print(f"Balance: {self.balance}")

    def yield_interest(self):
        self.balance =  self.balance + (self.balance * self.int_rate)
        return self

    @classmethod
    def all_balances(cls):
        sum = 0
        for account in cls.all_accounts:
            sum += account.balance
        return sum
    
    @staticmethod
    def can_withdraw(balance, amount):
        if (balance - amount) < 0:
            return False
        else:
            return True

Account_1 = BankAccount()
Account_2 = BankAccount()



Account_1.deposit(500).deposit(500).withdraw(200).yield_interest().display_account_info()
Account_2.deposit(300).deposit(600).withdraw(100).withdraw(200).withdraw(300).withdraw(100).yield_interest().display_account_info()
# Account_1.deposit(100)
# Account_1.withdraw(200)
# Account_1.display_account_info()