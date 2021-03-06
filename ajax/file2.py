num1 = 42 # variable declaration, integer
num2 = 2.3 # variable declaration, float
boolean = True # boolean, value
string = 'Hello World' # storing a string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # dictionary
fruit = ('blueberry', 'strawberry', 'banana') # list
print(type(fruit)) # type check
print(pizza_toppings[1])
pizza_toppings.append('Mushrooms') # key value
print(person['name']) # log
person['name'] = 'George' #log
person['eye_color'] = 'blue' #log
print(fruit[2]) # integer

if num1 > 45:
    print("It's greater")
else:
    print("It's lower") #conditional

if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!") #conditional

for x in range(5):
    print(x)
for x in range(2,5):
    print(x)
for x in range(2,10,3):
    print(x)
x = 0
while(x < 5):
    print(x)
    x += 1 #while loop conditional

pizza_toppings.pop() #pop
pizza_toppings.pop(1)

print(person)
person.pop('eye_color') #pop
print(person)

for topping in pizza_toppings: #conditional for loop
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

def print_hello_ten_times(): # function range
    for num in range(10):
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x): # function range
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10): #function range
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)