for countdown in range (5, 0, -1): #1
    print (countdown)


def my_function(x): #2
    return 1 + x

print(my_function(0))
print(my_function(1))

def first_plus_length(asd): #3
    return asd[0] + len(asd)

my_list = [1,2,3,4,5]
print(first_plus_length(my_list))

#4
#Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
#Example: values_greater_than_second([3]) should return False
def values_greater(this_list):
    if len(this_list) < 2:
        return False
    a = this_list[1]
    b = []
    for x in this_list:
        if x > a:
            b.append(x)
    return b
x = [5,2,3,2,1,4]
a = x[1]
print(a)
print(values_greater(x))


#5
#Example: length_and_value(4,7) should return [7,7,7,7]
#Example: length_and_value(6,2) should return [2,2,2,2,2,2]

def length_and_value(repeat = 1, num=0):
    print ([str(num) * repeat])
    
length_and_value(4,7)
length_and_value(6,2)


# # default parameters
# def greet(name = "", repeat = 2):
#     print(f"Good Morning {name} " * repeat)

# greet()
# greet("Shawn")
# greet("Shawn", 4)
# greet(4) # will this work

# # named arguments
# greet(repeat = 5)
# greet(name = "Tyler")
# greet(name = "Jim")
# greet(repeat = 30, name = "Jim")
# #length_and_value(6,2)