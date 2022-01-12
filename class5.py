class rectangle:
    def _init_(self):
        self.breadth
        self.length

    def size(self):
        self.area= self.length * self.breadth
        self.p=2*(self.length+self.breadth)
        print("Area of Rectangle: ", self.area)
        print("Perimeter of rectangle: ",self.p)
        return self.area
x=rectangle()
x.breadth=int(input("Enter the breadth:"))
x.length=int(input("Enter the length:"))
a=x.size()
y=rectangle()
y.breadth=int(input("Enter the breadth:"))
y.length=int(input("Enter the length:"))
b=y.size()
if(a>b):
    print("a is larger")
elif(a==b):
    print("a and b are same")
else:
    print("b is larger ")
