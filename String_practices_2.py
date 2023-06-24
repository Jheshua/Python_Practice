x = "Hola mundo" # Transform one lower case string to Upper case remember that Strings are immutable.
print(x.upper())

v = "Hello World" # Split a string in a List
v = v.split()
print (v)

# IMPORTANT -> We can also write "x." to see all the variables related with the method to costumize the String.



# Ways to "inject" variables into your String for printing: 
# There are two simple methods: .format() and f-strings for example:

print("This is a string {}" .format("INSERTED")) # This is going to insert the word INSERTED into the {} of the string

print("Hola {} {} {}" .format('fox','brown','quick')) 

print("Hola {f} {b} {q}" .format(q='fox',b='brown',f='quick')) # We can also asign variables inside of the .format()



#Float formatting follows "{value:width.precision f}"
result = 100/777 #result in float
print("The result was {r:1.3f}" .format(r=result)) #Same principles with the 1.3 as the previous string practices

#In a more recent version of python V3.6 they added a way to summarize the .format which is the following:
name="Jose" 
print(f"The result was {name}" ) #add and "F" at the beggining and then the same things {}

