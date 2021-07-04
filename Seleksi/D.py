iter = int(input())
res = 0
temp = 0
p_l = list(map(int,input().split()))
for y in p_l: 
    if y>res:
        temp = res
        res=y
print(temp*res)        