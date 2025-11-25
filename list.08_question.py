l=[1,6,9,7,8,4,3,2,5]
n=len(l)
for i in range(n-1):
    swap=False
    for j in range(0,n-i-1):
        if l[j]>l[j+1]:
            temp=l[j]
            l[j]=l[j+1]
            l[j+1]=temp
            swap=True
    if swap==False:
        print("list is sorted")
print(l)