import random
# 1. Write a program to read the text from a given file ‘poems.txt’ and find out whether it
# contains the word ‘twinkle’.

with open("Chapter8/poem.txt") as f:
    content=f.read()
    if("twinkle" in content):
        print("The word twinkle in the content..")
    else:
        print("The word twinkle not in the content..")

#======================================================================================================

# 2. The game() function in a program lets a user play a game and returns the score as an
# integer. You need to read a file ‘Hi-score.txt’ which is either blank or contains the previous
# Hi-score. You need to write a program to update the Hi-score whenever the game()
# function breaks the Hi-score.

def game():
    print("You are playing a game....")
    score = random.randint(1,62)  
    #fetch the hiscore
    with open("Chapter8/hiscore.txt") as f:
        hiscore= f.read()
        if(hiscore != ""):
             hiscore = int(hiscore)
        else:
             hiscore = 0

    print(f"Your Score {score}")
    if(score>hiscore):
         #write the file in hisscore
         with open("Chapter8/hiscore.txt","w") as f:
              f.write(str(score))
    return score

game()

#=====================================================================================================

# 3. Write a program to generate multiplication tables from 2 to 20 and write it to the different
# files. Place these files in a folder for a 13-year-old.

def generateTable(n):
    table=""
    for i in range(1,11):
        table += f"{n} X {i} = {n*i}\n"

    with open(f"Chapter8/tables/table_{n}.txt","w") as f:
        f.write(table)

for i in range(2,21):
    generateTable(i)

#===================================================================================================

# 4. A file contains a word “Donkey” multiple times. You need to write a program which
# replaces this word with ##### by updating the same file.

word = "donkey"

with open("Chapter8/file1.txt","r") as f:
    content =f.read()

contentNew = content.replace("donkey","####")

with open("Chapter8/file1.txt","w") as f:
    f.write(contentNew)

#==================================================================================================

# 5. Repeat program 4 for a list of such words to be censored.

words = ["donkey","animal","dangerous","very"]

with open("Chapter8/file1.txt","r") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#" * len(word))

with open("Chapter8/file1.txt","w") as f:
    f.write(content)


#=================================================================================================

# 6. Write a program to mine a log file and find out whether it contains ‘python’.

with open("Chapter8/log.txt","r") as f:
    content = f.read()

if("python" in content):
    print("Python is in the content")
else:
    print("Python is not in the content")

#================================================================================================

# 7. Write a program to find out the line number where python is present from ques 6.

with open("Chapter8/log.txt","r") as f:
    lines = f.readlines()

lineno=1
for line in lines:
    if("python" in line):
       print(f"Python is in the content,line no : {lineno}")
       break
    lineno += 1
else:
        print("Python is not in the content")

# -------------------------------------------------------------------------------------------------------

# 8. Write a program to make a copy of a text file “this.txt”.

with open("Chapter8/this.txt","r") as f:
    content = f.read()

with open("Chapter8/this_copy.txt","w") as f:
    f.write(content)

#------------------------------------------------------------------------------------------------------

# 9. Write a program to find out whether a file is identical and matches the content of another
# file.

with open("Chapter8/this.txt","r") as f:
    content=f.read()

with open("Chapter8/this_copy.txt","r") as f:
    content1=f.read()

if(content == content1):
    print("Yes these file are identicals")
else:
    print("No these file are identicals")

#=======================================================================================================

# 10. Write a program to wipe out the content of a file using python.
# remove in file contents

with open("Chapter8/this_copy.txt","w") as f:
    f.write("")

#===========================================================================================================
# 11. Write a python program to rename a file to “renamed_by_python.txt”.

with open("Chapter8/old.txt","r") as f:
   content= f.read()

with open("Chapter8/renamed_by_python.txt","w") as f:
   f.write(content)
