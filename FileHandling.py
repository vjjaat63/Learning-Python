"""
    Some important terms/arguements meanign

    r - open for reading (default)
    w - open for writing , clear the earlier data
    a - open for appending , add new data to the pre-existing data in the end
    x - create a new file and open it for writing
    + - open for updating (reading and writing)

    b - binary mode
    t - text mode (default)
    
    r+ - to read and ovewrite from starting    
    w+ - to read and delete previous ro write new
    a+ - to read and append

"""
f = open("file.txt","r") # r means read

data = f.read() # assingns the data of file to data
print(data)
# print(type(data))
f.close()

new = "Bankai Senbonzakura Kageyoshi \n"
f = open("file.txt","a")
f.write(new)
f.close()