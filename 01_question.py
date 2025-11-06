a="what are you doing"
c=a.split()
greater=c[0]
for i in c:
    if len(i)>len(greater):
        greater=i
print(greater)