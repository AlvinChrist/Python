pos = [1,0,0]
move = input()
if(len(move)<=50):
    for step in move:
        if step=="A":
            pos[0],pos[1]=pos[1],pos[0]
        elif step=="B":
            pos[1],pos[2]=pos[2],pos[1]
        elif step=="C":
            pos[0],pos[2]=pos[2],pos[0]
    print(pos.index(1)+1)
