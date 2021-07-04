rep = int(input())
for i in range(0,rep):
    ads = list(map(int,input().split()))
    if(ads[0]>ads[1]-ads[2]):
        print("do not advertise")
    elif(ads[0]==ads[1]-ads[2]):
        print("does not matter")
    else:
        print("advertise")