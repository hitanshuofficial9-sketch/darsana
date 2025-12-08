target=4
l=[1,2,3,4,9,5,6,8]
left=0
right=len(l)-1
while left<=right:
    mid=(left+right)//2
    if l[mid]==target:
        print(mid)
        break
    elif l[mid]<target:
        left=mid+1
    else:
        right=mid-1