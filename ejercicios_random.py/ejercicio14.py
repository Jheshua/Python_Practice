""" Ejercicio: Suma de múltiplos
Escribe una función en Python llamada suma_multiplos que reciba dos números enteros positivos, 
n y m. La función debe calcular la suma de todos los números enteros positivos menores que n que son múltiplos de m y 
devolver el resultado.

Por ejemplo, si n = 20 y m = 3, los múltiplos de 3 menores que 20 son 3, 6, 9, 12, 15 y 18. 
La suma de estos números es 63, por lo que el resultado esperado sería 63.

Aquí tienes un posible código para resolver este ejercicio: """

def suma(n, m):
    # n es el límite
    # m son los múltiplos
    multiplos = [ ]
    numeros = 1
    total_suma = 0
    while numeros < n:
        if numeros % m == 0:
            multiplos.append(numeros)
            total_suma = total_suma + numeros
        numeros = numeros + 1
    return multiplos, total_suma


print(suma(20, 3))
        
        