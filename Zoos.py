a=input()
l=len(a)
z,o=0,0
for i in a:
    if i=="z":
        z+=1
    else:
        o+=1
if z*2==o:
    print("Yes")
else:
    print("No")
    