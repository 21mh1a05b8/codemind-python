n,m=map(int,input().split())
l1=set(map(int,input().split()))
l2=set(map(int,input().split()))
k=l1.intersection(l2)
m=l1.union(l2)
l=m-k
print(len(l))