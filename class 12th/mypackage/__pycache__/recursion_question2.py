def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)

f=fact(3)
print(f)