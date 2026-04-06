def howmany(id,val):
    count=0
    for i in id:
        if i==val:
            count=count+1
    print(count)

id=[10,20,50,10,30]
val=10
howmany(id,val)