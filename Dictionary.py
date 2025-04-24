"""
    Dictionary is a key:value pair (as object in js) , they are unordered, mutable and keys are unique
    keys can be string,int,float or tuple (immutablle)
"""

me = {
    "name" : "Vishal Singh Jhajhris",
    "age" : 23,
    "marks" : [12,32,3,43,23],
    "male" : True
}
me["height"] = 6.1
print(me)
print(me["marks"])
print(me["marks"][2])

# Nested Dicitionary

myself = {
    "name" : {
        "fname" : "Vishal",
        "mname" : "Singh",
        "lname" : "Jhajhris",
        "nickname" : "Jaat"
    },
    "Subjects" : ["cpp","os","dbms"],
}

print(myself["name"]["nickname"])
print(myself["Subjects"][2])
print(me.keys())
print(myself.values())
print(me.items())
print(me.get("height"))
myself.update({"City":"Hisar"})
myself['name'].update({"Slogan" : "Bankai Senbonzakura Kageyoshi"})
"""
    Methods
    keys()  return all the keys
    values() return all the values
    items() return all key:value pairs
    get("key") return the value of key
    update({key:val}) add item to dictionary

"""

print(myself)