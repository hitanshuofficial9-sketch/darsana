def funstr(s):
    T=" "
    for i in s:
        if i.isdigit():
            T=T+i
        return T
    

x="PYTHON 3.9"
y=funstr(x)
print(x,y,sep="*")