class BankAccount:
    bank_name = "Rich Bank"
    all_accounts = []
    def __init__(self, int_rate = 0.2, balance = 0): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
    def deposit(self, amount):
        self.balance += amount
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


    @classmethod
    def all_balances(cls):
        sum = 0
        for account in cls.all_accounts:
            sum += account.balance
        return sum
    
    @staticmethod
    def can_withdraw(balance_amount):
        if (balance - amount) < 0:
            return False
        else:
            return True

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount()
        self.accounts = []
    
    def deposit(self,amount):
        self.account.withdraw(amount)
    
    def withdrawl(self, amount):
        self.account.deposit(amount)
    
    def display_user_balance(self):
        self.account.display_account_info()
        
user1 = User("Jessica","jessica.riley@gmail.com")

print(user1.account.balance)
user1.account.display_account_info()


