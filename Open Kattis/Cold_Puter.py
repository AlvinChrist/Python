iter = int(input())
sample = list(map(int,input().split()))
count = 0
for i in range(0,iter):
    count+=1 if sample[i]<0 else 0
print(count)    