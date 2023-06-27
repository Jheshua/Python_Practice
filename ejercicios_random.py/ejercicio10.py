#find the size of a string

def tama(stra):
    contador = 0
    word = list(stra)
    for letters in word:
        contador = contador +1 
    return contador

print(tama('holaaca'))
    
    