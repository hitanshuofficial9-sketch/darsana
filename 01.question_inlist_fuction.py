undo=[]
redo=[]
while True:
    text=input("enter your text")
    print("1:display text")
    print("2 undo")
    print("3 redo")
    redo.append(text)
    ch=int(input("enter your choice "))
    if ch==1:
        print(text)
    elif ch==2:
        if len(undo)==0:
            print("cant undo")
        else:
            print(undo[-1])
        l=redo.pop()
        undo.append(l)
    elif ch==3:
         print(redo[-1])
