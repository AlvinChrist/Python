iter = int(input())
count = 0
stop_count = False
for x in range(0,iter):
    roll = list(map(int,input().split()))
    if(roll[0]==roll[1]):
        count+=1
        if(count>=3):
            stop_count=True
    else:
        if not stop_count:
            count=0
print("Yes") if stop_count else print("No")            