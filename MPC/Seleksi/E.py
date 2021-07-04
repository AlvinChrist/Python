iter = int(input())
for x in range(0,iter):
    num = list(map(int,input().split()))
    if(num[0]>num[1]):
        print(">")
    elif(num[0]<num[1]):
        print("<")
    else:
        print("=")