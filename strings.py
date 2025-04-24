# temp = 'This is also a "string" '
# temp2 = """This is also a 'string' """
name = "Vishal Singh Jhajhria"
print(len(name))
print(name[3])
# name[3] = 't'  not possible can't change a string

# concatenation + , \t and \n , len(str)

# slicing

name2 = name[7 : ] # index 7 to end
name3 = name[ : 7] #index 0 to 6
name4 = name[ -8 : -1] #last index is -1
name6 = name[-14 : ]
# name5 = name[ -1:-8 ] 
#"name 4" = name[:]
print(name2)
print(name3)
print(name4)
# print(name5)
print(name6)
print(name)

#string funtions

name.endswith("ia") # return true if string ends with ia
name.capitalize()  # capitalize first word of the string
name.replace("Jhajhria" , "Jaat")  # replace all occurences of "Jhajhria" with "Jaat" but do not alter the original string
name.find("Singh") #Return 1st index of 1st occurence if not found return -1
name.count("a") #count the occurence of a
name.copy() # return the copy of name
print(name)