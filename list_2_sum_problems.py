l=[1,5,3,4,6,0,9,2]
target=int(input("enter your target"))
i=0
while i<len(l):
    j=i
    while j<len(l):
        if l[i]+l[j]==target:
            print(i,j)
            break
        j=j+1
    i=i+1    