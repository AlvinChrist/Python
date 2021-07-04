x = [1,1,1,1,2,2,3,3]
c = [0,0,0]
set = [1,2,3]
z = 0
for y in x:
    if y==set[z]:
        c[z]+=1
    else:
        z+=1
        if y==set[z]:
            c[z]+=1
print(c[0],c[1],c[2])