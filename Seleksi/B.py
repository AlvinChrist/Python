uang = int(input())
choices = int(input())
temp = [0,0,0,0]
for iter in range(0,choices):
    specs = list(map(int,input().split()))
    P = specs[0]
    R = specs[1]
    M = specs[2]
    H = specs[3]
    if H>uang:
        pass
    else:
        if P>temp[0]:
            temp = specs.copy()
        elif P==temp[0]:
            if R>temp[1]:
                temp = specs.copy()
            elif R==temp[1]:
                if M>temp[2]:
                    temp = specs.copy()
                elif M==temp[2]:
                    if H<temp[3]:
                        temp = specs.copy()
if temp==[0,0,0,0]:
    print("Eep tidak dapat membeli laptop")
else:
    print(*temp)                    