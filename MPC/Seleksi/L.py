size_one = int(input())
list_one = list(map(int,input().split()))
size_two = int(input())
list_two = list(map(int,input().split()))
list_one.sort()
list_two.sort()
res=[]
f = False
tmp_x=0
t = False
count=0
for x in range(0,size_two):
    if f:
        if count>1:
            res.append(list_one[tmp_x])
            count=0
        elif list_one[tmp_x]==list_two[x]:
            if(size_one==tmp_x+1):
                count+=1
            else:
                tmp_x+=1
        else:
            res.append(list_two[x])
    elif list_two[x]==list_one[x]:
        pass
    else:
        res.append(list_two[x])
        tmp_x=x
        f = True
res = set(res)
print(*res)
        
"""
    if f:
        if list_one[tmp_x]==list_two[x]:
            if count>1:
                res.append(list_one[tmp_x])
                count = 0
            elif tmp_x==size_one-1:
                count+=1  
            else:
                tmp_x+=1
        else:
            res.append(list_two[x])
    elif list_one[x]==list_two[x]:
        if size_one-1==x:
            f=True
        else:
            pass
    else:
        res.append(list_two[x])
        tmp_x=x
        f=True
"""
