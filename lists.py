#lists  are ordered sequences that can hold a variety of object types they use []

my_list = ["STRING", 100,23.3]
print(len(my_list)) # We can use "len" to see the length of the variable, in this case the list
print(my_list[0:2]) # we can also use the same concept of the range of the strings [1:3]


new_list = ["one","two","three","four"]
new_list.append("six") # We can use .append() to add something new at the end of the list
new_list.pop() #.pop() to delete something at the end 
new_list.pop(0) # if we want to delete something in specific, just write the index inside the pop

thenew_list = ["a","c","b","z","t","z",1,1,1,0,0,0,3,3,3]
thenew_list.sort() #we can also sort a list to make it easier to read.
thenew_list.reverse() # we can also reverse everything
print(thenew_list)
sum = thenew_list.count("1") #.count nos ayuda a detectar cuantos elemntos repetidos hay en esa lista
print(sum)


#these are the basic of lists but there are a lot more of thigns to explore related with lists just write the . and you will see all the options