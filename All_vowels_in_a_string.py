s=input()
a,c=0,0
if "a" in s and "e" in s and "i" in s and "o" in s and "u" in s:
    print(True)
    a=1
if "A" in s and "E" in s and "I" in s and "O" in s and "U" in s:
    print(False)
    c=1
if (a==0 and c==0):
    print(False)