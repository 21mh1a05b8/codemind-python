n=input()
n=n.split()
for i in n:
    for j in i:
        print(min(i),end=" ")
        print(max(i),end=" ")
        break