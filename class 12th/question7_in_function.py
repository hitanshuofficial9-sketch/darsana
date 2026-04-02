def change(P,Q=30):
    P=P+Q
    Q=P-Q
    print(P,"#",Q)
    return P

r=150
s=100
r=change(r,s)
print(r,"#",s)
s=change(s)