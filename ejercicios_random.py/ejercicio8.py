#Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter multiplicado por n. 
# Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".

entrada = int(input())
multiplicacion = int(input())
def generar_n_caracteres(n,x):
    resultado = entrada * multiplicacion
    return resultado
print(generar_n_caracteres(entrada,multiplicacion))
    
    