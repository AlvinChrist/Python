prime_list = []
while True:
    arr = list(map(int,input().split()))
    count=0
    if(arr[0]==0 and arr[1]==0):
        break
    else:
        for x in range(1,1001):
            if arr[0]<=x**2<=arr[1]:
                count+=1
    print(count)                