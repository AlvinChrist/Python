k = int(input())
arr = list(map(int,input().split()))
if arr[0]%k==0 or arr[1]%k==0:
    print("OK")
elif int(arr[1]/k)-int(arr[0]/k)>=1:
    print("OK")
else:
    print("NG")