s=input()
b,a,l,o,n=0,0,0,0,0
for i in s:
    if i=="b":
        b+=1
    elif i=="a":
        a+=1
    elif i=="l":
        l+=1
    elif i=="o":
        o+=1
    else:
        n+=1
print(min(b,a,l//2,o//2,n))