#show the even numbers in a list and print odd


#Even

def even(lst):
    for numbers in lst:
        if numbers % 2 == 0:
            print(numbers)
list = [1,2,3,4,5,6,7,8]
print(even(list))

# odd
def odd(lst1):
    for numbers in lst1:
        if numbers % 2 != 0:
            print(numbers)
list1 = [1,2,3,4,5,6,7,8,9]
print(odd(list1))
        