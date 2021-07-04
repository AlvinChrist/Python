stat = list(map(int,input().split()))
a=stat[0]
b=stat[1]
c=stat[2]
d=stat[3]
ans = [a*c,a*d,b*c,b*d]
print(max(ans))