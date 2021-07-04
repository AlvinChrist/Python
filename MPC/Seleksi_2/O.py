iter = int(input())
for x in range(0,iter):
    cmd = list(input().split())
    initial = [int(y) for y in cmd[1]]
    result = [int(z) for z in cmd[2]]
    steps = 0
    for wheel in range(0,int(cmd[0])):
        selisih = abs(initial[wheel]-result[wheel])
        if selisih>5:
            steps += 10-selisih
        else:
            steps+=selisih
    print("Case {}: {}".format(x+1,steps))