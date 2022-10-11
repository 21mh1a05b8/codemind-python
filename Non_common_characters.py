s1=set(input().lower())
s2=set(input().lower())
s=s1.intersection(s2)
k=s1.union(s2)
k=list(k)
c=0
for i in k:
    if i!=" ":
        if i not in s:
            c+=1
print(c)