#Playing with the values of a normal String 

# To show one specific letter of the String
MyString = "Hello World"
print(MyString[0]) # The result is going to be "H" since H is the number 0

#If we need from one point to another point we can use : to make the limits
MyString = "abcdefg"
print(MyString[1:5]) # The result is going to be from B to F (bcde)

#If we need other way to print all the String [::] this also works
MyString = "abcdefg"
print(MyString[::]) # The result is going to be all the String

#If we need other way to print all the String but 2 by 2 we add [::2] if we want 3 by 3 same thing
MyString = "abcdefg"
print(MyString[::2]) # The result is going to be all the String separated 2 by 2 (aceg)

#If we need other way to print all the String but 2 by 2 starting from an specific character, we add [2::2] 
MyString = "abcdefg"
print(MyString[2::2]) # The result is going to be all the String separated 2 by 2 but starting on the B (ceg)

#If we need a way to reverse a String we can use [::-1]
MyString = "abcdefg"
print(MyString[::-1]) # The result is going to be the reverse of the String, The first : means from the start, the second : means to the end.

#test github 