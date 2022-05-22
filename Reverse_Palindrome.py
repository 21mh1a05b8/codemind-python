def reverse(n):
    revnum=0
    while n>0:
        r=n%10
        revnum=(revnum*10)+r
        n=n//10
    return revnum
def palindrome(n):
    if reverse(n)==n:
        return n
def add(n):
    revnum=0
    while n:
        revnum=reverse(n)
        n+=revnum
        if palindrome(n):
            print(n)
            break
n=int(input())
add(n)