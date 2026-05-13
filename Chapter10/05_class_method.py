class Employee:
    a=5
    @classmethod  # class method use for attribute value not for instance value
    def show(cls):
        print(f"the value is attribute {cls.a}")

e = Employee()
e.a=45  # instance attributes

e.show()