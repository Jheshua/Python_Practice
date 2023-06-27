#Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en
# común o devuelva False de lo contrario. Escribir la función usando el bucle for anidado.
def superposicion(lst1,lst2):


    for numbers in lst1:
        for numbers1 in lst2:
            if numbers == numbers1:
                return True
            
    return False
normal1 = [1,2,3,4]
normal2 = [8,5,2,9]
print(superposicion(normal1,normal2))
                
                
            
    