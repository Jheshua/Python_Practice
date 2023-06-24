#Dictionaries are unordered mappings for storing objects, Dictionaries use a key-vallue pairing, this allo
#When to use a list and when to choose a dictionary?:
#Dictionaries are basically objects retrieved by a key name, unordered and cannot be sorted. 
#Lists are objects retrieved by location, so they are ordered sequences that can be indexed or sliced 


my_dict = {"Key1":"Value1","key2":"value2"}
my_dict["key3"] = "Value3" # if we want to add something in the dict we can use this funcion
print(my_dict.keys()) # if we want to see all the keys
print(my_dict.values()) # if we want to see all the values 
print(my_dict.items()) # if we want to see all the items separated in pairs

print(my_dict)

#there are more of funcions to explore, this is the same with lists, just write "." to see all the possible options to use