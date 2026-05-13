d = {} # empty dectionary

marks ={
    "Sachin":98,
    "Harish":24,
    "Rakesh":99,
    "Sanjay":85,
}

print(marks,type(marks))  # class <dict>
print(marks["Harish"])


# Two dictionary add
dict1 = {"Harish":77,"Rakesh":99}
dict2= {"Krish":66,"Sanjay":85}

dictMerge = dict1 | dict2

print(dictMerge)