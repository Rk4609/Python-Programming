try:
    a =int(input("enter a number :"))
    print(a)

except Exception as e:
    print(e)

else:   # try successfully run then run else block
    print("I am inside")