N = int(input())
c = 1
for a in range(1,N+1):
    for b in range(0,a):
        print(c,end=" ")
        if c<N:
            c+=1
        else:
            c=1
    print()