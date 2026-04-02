def lshift(arr,n):
    for i in range(0,n):
        y=arr[i]
        for j in range(0,len(arr)-1):
            arr[j]=arr[j+1]
        arr[len(arr)-1]=y
    print(arr)

arr=[10,20,30,40,12,11]
n=2
lshift(arr,n)