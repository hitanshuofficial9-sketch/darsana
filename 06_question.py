str=input("enter the string")
b=" "
c=".,/?!@"
for i in str:
    if i not in c:
        b=b+i.lower()
print(b)