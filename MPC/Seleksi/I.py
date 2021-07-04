def isSquareRoot(n):
    if(n!=0):
        m = int(n**(1/2))
        return m*m==n
    else:
        return False
trial = int(input())
for x in range(0,trial):
    cipher = input()
    if isSquareRoot(len(cipher)):
        c_r=int(len(cipher)**(1/2))
        text=""
        c=0
        for a in range(0,c_r):
            for b in range(0,c_r):
                text+=cipher[a+b*c_r]
        print(text)
    else:
        print("INVALID")