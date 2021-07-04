def is_prime(n):
    if n<=1:
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    i = 3    
    while i*i<=n:
        if n%i==0:  
            return False
        i+=2
        else:
     creturn True
    
iter = int(input())
arr = list(map(int,input().split()))
for x in arr:
    y = int(x**(1/2))
    if is_prime(y):
        if y*y==x:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")