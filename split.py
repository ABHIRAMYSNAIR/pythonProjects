n=input("Enter the string")
dict={}
s=n.split()
print(s)
for i in s:
    if i in dict:
        dict[i] = dict[i] + 1
    else:
        dict[i]=1
print(dict)