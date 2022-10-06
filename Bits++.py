n=int(input())
v="+"
s="-"
c=0
for i in range(n):
    k=input()
    k=list(k)
    for j in k:
        if j in v:
            c+=1
            break
        elif j in s:
            c-=1
            break
print(c)