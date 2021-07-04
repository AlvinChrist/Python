name=input()
prev=""
res = ""
for i in range(0,len(name)):
    #using ternary = 2x faster than if else!
    res+=name[i] if name[i]!=prev else ""
    #if(name[i]==prev):
    #    pass
    #else:
    #    res+=name[i]
    prev=name[i]
print(res)        
    