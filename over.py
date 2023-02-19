n=int(input("Enter the size"))
x=[]
print("Enter the elements of list")
for i in range(0,n):
    y=int(input())
    if(y>100):
        x.append("over")
    else:
        x.append(y)
print(x)