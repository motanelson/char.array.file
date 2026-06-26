print("\033c\033[47;31m/give me the class file to view ? ")
a=input().strip()
#a="Hello.class"
f1=open(a,"rb")
b=f1.read()
f1.close()
j=False
for c in b:
    if c>31 and c<129:
        cc=chr(c)
    
        print(cc,end="")
        j=True
    else:
        if j:
            print("")
            j=False