n=input()
n=n.split()
m=[]
mi=[]
s,s1=0,0
for i in n:
    m.append(max(i))
    mi.append(min(i))
for i in m:
    s+=ord(i)
for i in mi:
    s1+=ord(i)
print(abs(s1-s))