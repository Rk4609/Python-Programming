# single line read using --readline
f = open("Chapter8/file.txt")

line=f.readline()
print(line)
line1=f.readline()
print(line1)
line2=f.readline()
print(line2)
line3=f.readline()
print(line3)
f.close()


#using while loops--readline
f = open("Chapter8/file.txt")
line = f.readline()
while(line != ""):
    print(line)
    line= f.readline()

f.close()




#multiple line read using-- readlines
f = open("Chapter8/file.txt")

lines=f.readlines()
print(lines)

f.close()
