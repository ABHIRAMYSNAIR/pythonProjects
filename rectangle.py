class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return (self.length*self.breadth)
    def perimeter(self):
        return (2*(self.length+self.breadth))
print("FIRST RECTANGLE")
l=int(input("Enter the length : "))
b=int(input("Enter the breadth : "))
x=rectangle(l,b)
y=x.area()
z=x.perimeter()
print("the area is",y)
print("the perimeter is",z)
print("________________")
print("SECOND RECTANGLE")
l1=int(input("Enter the length : "))
b1=int(input("Enter the breadth : "))
x1=rectangle(l1,b1)
y1=x1.area()
z1=x1.perimeter()
print("the area is",y1)
print("the perimeter is",z1)
print("________________")
if(y>y1):
    print("The first rectangle is greater than second rectangle")
else:
    print("The second rectangle is greater than first rectangle")
