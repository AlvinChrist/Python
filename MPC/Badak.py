jarak = int(input())
step = 0
i = 0
for i in range(5,0,-1):
    if(jarak%i!=0 and jarak>i):
        step += int(jarak/i)
        jarak = jarak-step*i
    elif(jarak%i==0):
        step += jarak/i
        break
        
print(int(step))
