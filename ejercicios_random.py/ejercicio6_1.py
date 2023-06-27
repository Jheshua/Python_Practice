def es_palindromo(palabra):
    normal = list(palabra.lower())  # Convertir la palabra en una lista de caracteres
    
    reverso = normal[::-1]  # Crear una lista invertida
    
    if normal == reverso:  # Comparar ambas listas
        return True
    else:
        return False

print(es_palindromo('Somos'))