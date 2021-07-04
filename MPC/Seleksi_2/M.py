iter = int(input())
solution = 0
for x in range(0,iter):
        problem = list(map(int,input().split()))
        y = 0
        for z in problem:
            y+=z
        if y>=2:
            solution+=1
print(solution)            