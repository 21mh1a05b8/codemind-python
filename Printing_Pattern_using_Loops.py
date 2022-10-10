n=int(input())
k=(2*n)-1
l=0
h=k-1
v=n
mat=[[0 for i in range(k)] for j in range(k)]
for i in range(n):
    for j in range(l,h+1):
        mat[i][j]=v
    for j in range(l+1,h+1):
        mat[j][i]=v
    for j in range(l+1,h+1):
        mat[h][j]=v
    for j in range(l,h+1):
        mat[j][h]=v
    l=l+1
    h=h-1
    v=v-1
for i in range(k):
    for j in range(k):
        print(mat[i][j],end=' ')
    print()