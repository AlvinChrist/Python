from math import ceil
test = int(input())
for i in range(0,test):
    num = list(map(int,input().split()))
    if(num[1]>num[0]):
        print(int(num[1]-num[0]))
    else:
        i = ceil(num[0]/num[1])
        print(num[1]*i-num[0])