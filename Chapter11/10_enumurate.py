l =[22, 33, 556,66,46]
#directly
index =0
for item in l:
    print(f"the list in index {index} and {item}")
    index += 1

#using enumurate
for index,item in enumerate(l):
    print(f"the list in index {index} and {item}")
