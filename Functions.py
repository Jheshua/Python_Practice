def say_hello(name):
    print(f"Hello{name}")
    
say_hello("jose")

def add_num(num1,num2):
    print(num1+num2) 
    return(num1+num2) # The difference between print and return is that return allow us to save this in a variable and print only shows the result 
    #result = add_num (num1+num2)

add_num(10,20)

#Example 1: 
def check_even_list(num_list):
    #returning all the even numbers in a list
    even_numbers = []
    for number in num_list:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            pass
    return even_numbers

result = check_even_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(result)
#--------------------
def hi(name):
    print(f"Hello! {name}")
hi("Jheshua")
#--------------------
def myfunc(x,y,z):
    if z == True:
        return x
    else:
        return y
result = myfunc("hello", "Goodbye", True)
print (result)

#--------------------

def maths(a,b):
    print(a+b) # actually showing us the result
maths(1,2)

def maths1(a,b):
    return a+b  #returning something in the console
result = maths1(2,3)
print (result)

#--------------------

def is_even1(h):
    if h % 2 == 0:
        return True
    else:
        return False
is_even1(2)
#--------------------

def is_greater(t,y):
    if t <= y:
        return False
    else:
        return True
result3 = is_greater(6,5)
print(result3)