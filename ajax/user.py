class User:
    bank_name = "Jessica's Bank"
    def __init__(self, name):
        self.name = name
        self.account_balance = 0
    
    def make_deposit(self,amount):
        self.account_balance += amount
        return self
    
    def make_withdrawl(self, amount):
        self.account_balance -= amount
    
    def display_user_balance(self):
        # print(f"User:{self.name}, Balance: ${self.account_balance}")
        return f"User:{self.name}, Balance: ${self.account_balance}"
        

jessica = User("Jessica Riley")
elsa = User("Elsa")
eren = User("Eren")
print(jessica.name)

jessica.make_deposit(500)
jessica.make_deposit(300)
jessica.make_deposit(900)
jessica.make_withdrawl(100)
elsa.make_deposit(700)
elsa.make_deposit(500)
elsa.make_withdrawl(100)
elsa.make_withdrawl(50)
eren.make_deposit(1000)
eren.make_withdrawl(100)
eren.make_withdrawl(50)
eren.make_withdrawl(200)

print(jessica.display_user_balance())
print(elsa.display_user_balance())
print(eren.display_user_balance())



# class User:
#     # class attributes get defined in the class 
#     bank_name = "First National Dojo"
#     # now our method has 2 parameters!
#     def __init__(self, name, email_address):
#     	# we assign them accordingly
#         self.name = name
#         self.email = email_address
#     	# the account balance is set to $0
#         self.account_balance = 0
# guido = User("Guido van Rossum", "guido@python.com")
# monty = User("Monty Python", "monty@python.com")
# print(guido.name)	# output: Guido van Rossum
# print(monty.name)	# output: Monty Python

# class User:		# here's what we have so far
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#         self.account_balance = 0
#     # adding the deposit method
#     def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
#     	self.account_balance += amount	# the specific user's account increases by the amount of the value received

# guido.make_deposit(100)
# guido.make_deposit(200)
# monty.make_deposit(50)
# print(guido.account_balance)	# output: 300
# print(monty.account_balance)	# output: 50

