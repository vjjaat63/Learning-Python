name = "Vishal"
midname = "Singh"
lastname = "Jhajhria"
age = 23
height = 6.1
partner = None
male = True

# print(type(name) + type(midname) + type(lastname)+ type(age) + type(height) + type(partner) + type(male))
print(type(name) , type(midname) , type(lastname), type(age) , type(height) , type(partner) , type(male))

# print(name + " " + midname + " " + lastname + " is " + age + " years old.") Error
print(name + " " + midname + " " + lastname + " is " + str(age) + " years old.")
print(name + " " + midname + " " + lastname + " is " , age , " years old.")