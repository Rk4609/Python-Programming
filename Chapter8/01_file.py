
f = open("Chapter8/file.txt")   # module is not declare
data = f.read()
print(data)
f.close()


# open two files and process together
with(
   open("Chapter8/file.txt") as f1,
   open("Chapter8/file1.txt") as f2):

   data1= f1.read()
   data2= f2.read()

   print(data1)
   print(data2)



# The random-access memory is volatile, and all its contents are lost once a program terminates. In order to
# persist the data forever, we use files.
# A file is data stored in a storage device. A python program can talk to the file by reading content from it and
# writing content to it.

# There are 2 types of files:
# 1. Text files (.txt, .c, etc)
# 2. Binary files (.jpg, .dat, etc)


# Modes Of Opening A File
# r – open for reading
# w - open for writing
# a - open for appending
# + - open for updating.
# ‘rb’ will open for read in binary mode.
# ‘rt’ will open for read in text mode.