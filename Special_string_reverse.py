n=input()
n=list(n)
i=0
j=len(n)-1
while i<j:
    if n[i].isalpha()==False:
        i+=1
    elif n[j].isalpha()==False:
        j-=1
    else:
        n[i],n[j]=n[j],n[i]
        i+=1
        j-=1
n=''.join(n)
print(n)