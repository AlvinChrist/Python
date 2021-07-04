N = int(input())
matriks = [[1 for x in range(0,N)]for y in range(0,N)]
for x in range(1,N):
    for y in range(1,N):
        matriks[x][y]=matriks[x][y-1]+matriks[x-1][y]

for a in matriks:
    print(a)