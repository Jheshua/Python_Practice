# Python | Multiply all numbers in the list

def multi(lst):
    total = 1
    for numbers in lst:
        total = total * numbers
    return total
lista = [2,3,4]
print(multi(lista))
        
        