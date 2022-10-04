n=input()
n=n.split()
for i in n:
    a=ord(min(i))
    b=ord(max(i))
    print(abs(b-a),end=" ")