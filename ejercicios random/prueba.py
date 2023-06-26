#Sumar el total de los numeros pares e impares entre 1 y N

x = int(input('Digite el numero hasta cual desea calcular: '))
numero_par = 0
numero_impar = 0
for i in range(2,x+1,2):
    numero_par += i 
    
print('la suma de los pares es: ', numero_par)    
for a in range(1,x+1,2):
    numero_impar += a 
    
print('la suma de los impares es: ', numero_impar)
        