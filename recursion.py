def fact(n):
    if(n==1 or n==0):
        return 1
    return n*fact(n-1)

def sum(n):
    if(n==0):
        return 0
    return n+sum(n-1)

num = int(input("Enter a number : "))
print("Factorial of",num,"is : " ,fact(num))
print("Sum of first",num,"numbers is : ",sum(num))

def listvalues(li,ind):
    if(ind == len(li)):
        return
    print(li[ind])
    listvalues(li,ind+1)

li = [1,4,5,6,True,"Vishal",6.1]
print("The values of the list are : " )
listvalues(li,0)