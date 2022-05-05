n=int(input())
import math
s=math.sqrt(n)
if int(s+0.5)**2==n:
    print("True")
else:
    print("False")