"""
list == array but can hold multiple data types
strings are immutable but lists are mutable
"""
""" Methods
    append(value) insert value at end
    insert(idx,val) insert val at index idx
    sort() increasing order sort
    sort(reverse = True) decreasing order sort
    reverse() reverse
    remove(val) remove first occurence of 1
    pop(idx) remove value at index idx
"""
marks = [10,3,2,7,9,6,7,8]
print(marks)
print(type(marks))
print(len(marks))
marks[0] = "Vishal"
print(marks)
marks.reverse()
print(marks)
print(marks[:2])
print(marks)