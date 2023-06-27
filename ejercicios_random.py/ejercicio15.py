
def cositas(lst):
    pares = []
    for i in lst:
        if i % 2 == 0:
            pares.append(i)
    return pares
lista = [1,2,3,4,5,6,7]
print(cositas(lista))