"""
    Some important terms/arguements meanign

    r - open for reading (default)
    w - open for writing , clear the earlier data
    a - open for appending , add new data to the pre-existing data in the end
    x - create a new file and open it for writing
    + - open for updating (reading and writing)

    b - binary mode
    t - text mode (default)

"""
f = open("learning python/file.txt","r") # r means read

data = f.read() # assingns the data of file to data
print(data)
# print(type(data))
f.close()