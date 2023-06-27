#Escribir una función sum() y una función multip() que sumen y 
# multipliquen respectivamente todos los números de una lista. Por ejemplo: sum([1,2,3,4])
# debería devolver 10 y multip([1,2,3,4]) debería devolver 24.

def sum(lst):
    suma_total = 0
    for i in lst:
        suma_total += i 
    return suma_total
        
#example of usage
lista = [1,2,3,4]
print(sum(lista))
#-----------------------------------------
def multip(lst):
    suma_total = 1
    for i in lst:
        suma_total =  suma_total * i 
    return suma_total
        
#example of usage
lista = [1,2,3,4]
print(multip(lista))