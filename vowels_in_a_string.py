n=input()
c=input()
f=0
for i in range(len(n)):
    if n[i]==c:
        print(True)
        print(i)
        f+=1
        break
if f==0:
    print(False)