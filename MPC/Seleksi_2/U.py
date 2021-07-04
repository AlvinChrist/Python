a = input()
b = input()
res = ""
for x in range(0,len(a)):
    if a[x]!=b[x]:
        res+="1"
    else:
        res+="0"
print(res)        