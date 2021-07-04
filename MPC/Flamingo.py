trial = int(input())
buf = 0
for i in range(0,trial):
    op = input()
    if "++" in op:
        buf+=1
    else:
        buf-=1
print(buf)
    