iter = int(input())
for x in range(0,iter):
    N = input()
    arr = list(map(int,input().split()))
    if 0 in arr:
        print("0")
    else:
        arr.sort(reverse=True)
        res = 1
        for num in arr:
            res *=num
        print(res)