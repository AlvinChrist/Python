iter = int(input())
candles = 0
for x in range(0,iter):
    sample = list(map(int,input().split()))
    candles = sample[1]*((3+sample[1])/2)
    print("{} {}".format(sample[0],round(candles)))