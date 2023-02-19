n=input("Enter the strings")
dict={}
for i in n:
    if i in dict:
        dict[i]=dict[i]+1
    else:
        dict[i]=1
print(dict)
print("character frequency")
for m,n in dict.items():
    print(m,n)