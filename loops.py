#while loop

i = 1
while i<=10:
    print(i)
    i += 1

tup = (1,4,9,16,25,36,49,64,81,100)

ind = 0
num = int(input("Enter the number to search in tup : "))
found = False

while ind<len(tup):
    if(tup[ind] == num):
        found = True
    ind+=1
if found:
    print("Number is in the tuple")
else:
    print("number not found in the tup")


# break and continue - same as always

for n in tup:
    print(n)

# range(start , end, increment)

for i in range(5):  # 0,1,2,3,4
    print(i)

for i in range(1,5): #  1,2,3,4
    print(i)

for i in range(1,5,2): # 1,3
    print(i)

# pass : use as a placeholder for future code

for i in range(100,0,-1):
    pass