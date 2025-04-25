# read() and readline()
# after reading all data using read pointer goes to the end and there is left nothing to read and we get an empty line

f = open("file.txt","r")
"""
data = f.read()
print(data)

if we uncomment this the below commands will not work as it will read all data and points to the end of file
"""

line1 = f.readline()
print(line1)

line2 = f.readlines()  # read all the remaining lines and return a list
print(line2)

print(type(line2))

f.close()