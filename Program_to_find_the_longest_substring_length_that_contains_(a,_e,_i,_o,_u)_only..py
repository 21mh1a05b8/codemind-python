n=input()
v="aeiou"
m,c=1,0
for i in range(0,len(n)):
    if n[i] in v:
        c+=1
    else:
        c=0
    m=max(m,c)
print(m)       