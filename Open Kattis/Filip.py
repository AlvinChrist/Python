res = [0,0]
text = list(map(str,input().split()))
for x in range(0,2):
    b = ""
    for y in range(0,3):
        b += text[x][2-y]
    res[x] = int(b)
print(res[0] if res[0]>res[1] else res[1])