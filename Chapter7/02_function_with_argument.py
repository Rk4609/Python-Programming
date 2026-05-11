# name is paramater and calling in argument pass

def goodDay(name ,age, ending):
    print(" Good Day," + name)
    print(f"My age is : {age}")
    print(ending)


goodDay("Rakesh",22,"Thank you")
goodDay("Sachin",24,"Thank you")
goodDay("Lalit",24,"Thank you")


# return value concept
def goodDay(name ,age, ending):
    print(" Good Day," + name)
    print(f"My age is : {age}")
    print(ending)
    return "ok"


a=goodDay("Rakesh",22,"Thank you")
print(a)

