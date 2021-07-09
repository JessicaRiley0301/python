class User: #chainingmethods
    bank_name = "Jessica's Bank"
    def __init__(self, name):
        self.name = name
        self.account_balance = 0
    
    def make_deposit(self,amount):
        self.account_balance += amount
        return self
    
    def make_withdrawl(self, amount):
        self.account_balance -= amount
        return self
    
    def display_user_balance(self):
        print(f"User:{self.name}, Balance: ${self.account_balance}")
    

jessica = User("Jessica Riley")
elsa = User("Elsa")
eren = User("Eren")
print(jessica.name)

jessica.make_deposit(500).make_deposit(300).make_deposit(900).make_withdrawl(100)
elsa.make_deposit(700).make_deposit(500).make_withdrawl(100).make_withdrawl(50)
eren.make_deposit(1000).make_withdrawl(100).make_withdrawl(50).make_withdrawl(200)

print(jessica.display_user_balance)
print(elsa.display_user_balance())
print(eren.display_user_balance())