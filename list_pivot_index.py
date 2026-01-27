l=[1,2,4,5]
x=[]
for i in range(0,len(l)):
    left_sum=0
    right_sum=0
    for j in range(i+1,len(l)):
        right=right_sum+l[j]
    for k in range(0,i-1):
        left_sum=left_sum+l[k]
    if left_sum==right_sum:
        print(i)
        break