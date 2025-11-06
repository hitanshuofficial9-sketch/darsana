a="what are you"
c=a.split()
smallest=c[0]
for i in c:
    if len(i)<len(smallest):
        smallest=i
print(smallest)