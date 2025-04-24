# its a choice whether to return something or not

# inbuilt - print(),len(),type(),range(),etc.

# user-defined : defined by user



def ln(a):  # prog to print length of list by user defined fn
    i = 0
    for el in a:
        i+=1
    return i

def one_line(a): # print all list values in one line
    s = ""
    for el in a: 
        s += str(el) + " "
    return s

ls = [1,2,3,43,5,5, "I"]
st = {1,2,2,2,233,4,5,7,"Jaat"}
print(ln(ls))
print(ln(st))

print(one_line(ls))
print(one_line(st))