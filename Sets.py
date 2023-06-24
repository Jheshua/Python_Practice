# Sets are unordered collections of unique elements
# meaning there can only be one representative of the same object 

myset = set()
myset.add(1)
myset.add(2)
mylist = [1,1,1,2,2,2,3,3,3,4] #We can make a list and transform it using set() 
print(set(mylist)) # this is going to give me the set of the unique values


print(set("Mississippi")) # this is going to give me a set of unique letters
print(set([1,1,2,3]))

#comentario de prueba