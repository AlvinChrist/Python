iter = int(input())
val = {
    "C" : 12.01,
    "H" : 1.008,
    "O" : 16.00,
    "N" : 14.01

}
for x in range(0,iter):
    chem = input()
    temp = ""
    total = 0
    y=0
    for y in range(0,len(chem)):
        if(chem[y].isalpha()):
            total+=val[chem[y]]
            temp=chem[y]
        else:
            if(y+1!=len(chem) and not chem[y+1].isalpha()):
                num = int(chem[y]+chem[y+1])
                total+=(num-1)*val[temp]
                y+=1
            elif(chem[y-1].isalpha()):
                total+=(int(chem[y])-1)*val[temp]
    print("%0.3f" %(round(total,3)))