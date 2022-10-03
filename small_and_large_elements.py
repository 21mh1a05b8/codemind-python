n=input()
n=n.split()
print(*min(n[0]),end=" ")
print(*max(n[len(n)-1]))