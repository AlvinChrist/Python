stat = list(map(int,input().split()))
if(stat[0]%2==0):
    if(stat[0]/2>=stat[1]):#it's odd number
        print(2*stat[1]-1)
    else: #it's even number
        print((int(stat[1]-stat[0]/2))*2)
else:
    if(int(stat[0]/2+0.5)+0.5>=stat[1]):
        print(2*stat[1]-1)
    else:
        print((stat[1]-int(stat[0]/2+0.5))*2)
