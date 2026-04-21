def febo(n):
    if n<=0:
        return 1
    return febo(n-1)+febo(n-2) 

x=febo(5)
print(x)

def fibo(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
    
t=fibo(5)
print(t)