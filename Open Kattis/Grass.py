c = float(input())
iter = int(input())
width=0
for i in range(0,iter):
    area = list(map(float,input().split()))
    width+=area[0]*area[1]
print(width*c)