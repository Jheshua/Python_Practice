x = int(input(""))
for i in range(x):
    word = input("")
    
    if (len(word) > 10 ):
        abb = word[0] + str(len(word)-2) + word[-1] 
        print(abb)
    else:
        print(word)
    

#Veredicto problem 71A -> ACCEPTED 
