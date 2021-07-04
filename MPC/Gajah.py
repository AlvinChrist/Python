num = list(map(int,input().split()))
a = 0
b = 0
c = 0
num.sort()
c = (num[2]+num[1]-num[0])/2
b = num[1]-c
a = num[0]-b
print("{} {} {}".format(int(a),int(b),int(c)))