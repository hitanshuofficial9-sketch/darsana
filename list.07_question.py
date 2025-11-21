l=[1,2,3,4,5,6,7]
key=int(input("enter your number"))
found=False
for i in range(0,len(l)):
    if l[i]==key:
        found=True
        print(f"{key} found at position{i+1}")
        break
if found==False:
    print(f"{key}not found")