#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
# guess 5 answer 5

#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
#guess none answer undefined

#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
#guess 5 answer 5

#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
#guess 5 answer 5

#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
# guess 5, none answer 5 none

#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
#guess 3 , 5 answer 3 5 unsupported

#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
# guess 2 , 5 answer 25

#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
#guess 100, 10 answer 100 , 10

#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
#guess 7 , 14 , 21 answer 7 , 14, 21

#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
#guess 8 answer 8

#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
#guess 500 , 300 , 300 , 300, answer 500 500 300 500
#i don't get this one

#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
#guess 500, 300, 300 300 answer 500 500 300 500

#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
#guess 500 300 500 300 answer 500 500 300 300
#i dont get this one either

#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
#guess 1 3 2 1 answer  1 3 2

#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
#guess 1 3 5 10 answer 