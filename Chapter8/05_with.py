#mainly uses 

f =open("Chapter8/file.txt") 
print(f.read())
f.close()

#The same can be written using with statement like this :

with open("Chapter8/file.txt") as f:
    print(f.read())

    #you dont have to close file