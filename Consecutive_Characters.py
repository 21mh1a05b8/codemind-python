n=input()
c,m=0,1
for i in range(1,len(n)):
    if n[i]==n[i-1]:
        c+=1
        if c>m:
            m=c
    else:
        c=1
print(m)