marks ={
    "Sachin":98,
    "Harish":24,
    "Rakesh":99,
    "Sanjay":85,
}

print(marks.items()) #list of key value (tuples)
print(marks.values())  #values-98,24
print(marks.keys()) #key-sachin,harish
marks.update({"Harish":45,"Ravi":88})  #new add and update in dict
print(marks)
# print(marks.get("Sachin2")) #prints none
# print(marks["Sachin2"])  #return an error
print(marks.clear()) # dict is clear 
