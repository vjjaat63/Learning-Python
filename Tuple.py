#Tuples are inbuilt data types in python which are similar to lists but are immutable

marks = [1,2,3,4,5,4,3,2,1,0] # list
mark = (1,3,4,5,4,3,2,1,0) # tuple

print(mark[3])
# mark[3] = 10 not possible
mrk = (1,) # single value tuple declaration so always use a , but in case of multiple values it is a choice

print(mark[1: 5])

# index and count

print(mark.index(2)) # index(val) return first index where value is available
print(mark.count(0)) # count(val) return the number of occurences of value

a = input("Enter name of movie 1 : ")
b = input("Enter name of movie 2 : ")
c = input("Enter name of movie 3 : ")

movies = [a,b,c]

print(movies)