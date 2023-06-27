#Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el mismo aspecto escritas 
# invertidas), ejemplo: es_palindromo ("radar") tendría que devolver True.

def es_palindromo(palabra):
    normal = [] #we save the word in normal order
    reverso = [] #we save the word inverted 
    for letra in palabra:
        normal.append(letra) # adding the word to the list
        reverso.append(letra)
        
    reverso.reverse() #reversing the word in the list (reverso)
    

    if normal == reverso : #comparing both lists 
        return True
    else:
        return False
    

print(es_palindromo('Somos')) #result 

