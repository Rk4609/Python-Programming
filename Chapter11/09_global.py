a = 99  #global variable running is all places
def fun():
    # a is llocal variable for running in this function
    global a  # changes in locall a
    a = 6
    print(a)

fun()
print(a)
