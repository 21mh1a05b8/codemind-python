a=input()
d='0123456789'
sum=0
for i in a:
    if i.isdigit()==True:
        z=int(i)
        sum=sum+z
print(sum)