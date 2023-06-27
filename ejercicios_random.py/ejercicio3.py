#Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.

def characters(st:str):
    my_dict = {'a','e','i','o','u'}
    if st in my_dict:
        return True
    else:
        return False
#Example of usage
print(characters('u'))