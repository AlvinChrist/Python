while True:
    koordinat = list(map(int,input().split()))
    x1 = koordinat[0]
    y1 = koordinat [1]
    x2 = koordinat[2]
    y2 = koordinat[3]
    steps = 0
    if x1+x2+y1+y2==0:
        break
    elif abs(x1-x2)==abs(y1-y2)!=0:
        steps=1
    else:
        if abs(x1-x2)>0:
            steps+=1
        if abs(y1-y2)>0:
            steps+=1
    print(steps)