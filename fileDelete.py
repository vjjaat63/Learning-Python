"""
    Deleting a file require to import os module
"""

#create and write in a file
try:
    f = open("temp.txt","x")
    f.write("You can never see this file")
    f.close()
    import os
    os.remove("temp.txt")
except FileExistsError as e:
    print("File ' temp.txt 'already exists",e)
    