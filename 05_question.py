str=input("enter the string")
b=" "
for i in range(0,len(str),2):
    b=b+str[i]
    if (i<len(str)-1):
        b=b+str[i+1].upper()
print(b)
