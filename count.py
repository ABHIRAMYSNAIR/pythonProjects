n=int(input("Enter the number of string"))
print("enter the string ")
x=[]
count=0
for i in range (0,n):
    y=input()
    x.append(y)
print(x)
for i in x:
   for j in i:
       if(j=='a'):
           count=count+1
print("occurance of A=",count)