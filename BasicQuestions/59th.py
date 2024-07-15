class Test:
    def __init__(self) -> None:
        #Those a and b are instance variable.
        self.a = 10
        self.b = 20

    def m1(self):
        self.c = 30
    
t = Test()
# Because we are not calling method. After  calling  the methods.
t.m1()

# if need to add more element from outside of class.
t.d = 40
t.e = 50
print(t.__dict__)