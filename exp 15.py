a=[1,2,3,4,5]
b=[6,0,2,5,7]
if len(a)==len(b):
    print("both the list are of same length")
else:
    print("both list are not of same length")
if (sum(a)==sum(b)):
    print("both the list sums to same value")
else:
    print("both the list not sums to same value")
print("common elements")
for x in a:
    for y in b:
        if(x==y):
            print(y)