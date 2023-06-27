#Python program to find smallest number in a list and the highest numbers 

def menor(lst):
    menorcito = lst[0]  # Asignar el primer elemento del arreglo
    for i in lst:
        if i <= menorcito:
            menorcito = i
    return menorcito
lista = [23,12,3,4]
print(menor(lista))


#ver el mayor

def mayor(lst):
    mayorcito = lst[0]
    for numbers in lst:
        if numbers >= mayorcito:
            mayorcito = numbers
    return mayorcito
lista1 = [1,2,3,4,5,6,7]
print(mayor(lista1))
        