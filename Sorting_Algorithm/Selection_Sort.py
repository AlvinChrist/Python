arr = [9,8,7,6,5,4,3,2,1]

for i in range(0,len(arr)):
    currPos=i
    for j in range(i+1,len(arr)):
        if(arr[j]<arr[currPos]):
            currPos=j
    if(currPos!=i):
        arr[currPos],arr[i]=arr[i],arr[currPos]
    print(*arr)
    print()