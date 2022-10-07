n=input()
n=list(n)
v="aeiouAEIOU"
i=0
j=len(n)-1
while i<j:
    if n[i] not in v:
        i+=1
    elif n[j] not in v:
        j-=1
    else:
        n[i],n[j]=n[j],n[i]
        i+=1
        j-=1
n="".join(n)
print(n)