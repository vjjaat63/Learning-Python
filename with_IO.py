"""
with() is also used for reading and writing purposes but it defines a scope for the file

with open("file.txt","w") as f  is same as f = open("file.txt","w")
with open("file.txt","r") as f  is same as f = open("file.txt","r")

"""
with open("file.txt","r")as f:
    data = f.read()
    print(data)

with open("file.txt","w") as f:
    f.write("Kaioken")
    
with open("file.txt","r") as f:
    data = f.read()
    print(data)