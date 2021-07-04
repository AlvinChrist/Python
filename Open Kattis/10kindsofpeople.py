class Matriks:
    def __init__(self,baris,kolom):
        self.baris = baris
        self.kolom = kolom
        self.matriks = [['' for i in range(0,kolom)] for j in range(0,baris)]
    
    def set(self,val): #mengisi data matriks mulai dari baris 1 kolom 1
        if(len(val)==self.baris*self.kolom):
            b=0 
            k=0
            for v in val:
                self.matriks[b][k]=v
                k+=1
                if(k==self.kolom): #ketika sudah mencapai kolom terakhir , pindah ke baris selanjutnya 
                    b+=1#dan mengulang hitungan kolom dari 1 lagi
                    k=0
    def value(self,b,k): #return data matriks baris ke b dan kolom ke k
        return self.matriks[b-1][k-1]
     
    def find(self,value): #mencari letak satu nilai spesifik pada matriks
        coordinate_map=[]
        for b in range(1,self.baris+1):
            for k in range(1,self.kolom+1):
                if(A.value(b,k)==value):
                    coordinate_map.append([b,k])
        return coordinate_map

def walk(state,x1,y1,x2,y2,a_coordinate):
    #print(a_coordinate)
    try:
        if(x1==x2 and y1==y2):
            return state
        n_spot = [] 
        a_coordinate.remove([x1,y1])
        for spot in a_coordinate:
            if((abs(x1-spot[0])==1 and y1-spot[1]==0)or(x1-spot[0]==0 and abs(y1-spot[1])==1)):#memungkinkan pergerakan ke atas bawah kiri kanan namun tidak diagonal
                n_spot.append(spot)
        #print(n_spot)
        if(len(n_spot)>0):
            for spot in n_spot:
                #print("from ({},{}) to ({},{})".format(str(x1),str(y1),str(spot[0]),str(spot[1])))
                res=walk(state,spot[0],spot[1],x2,y2,a_coordinate)
                if(res==state):
                    return state
    except ValueError:
        return 2

                
ukuran = list(map(int,input().split())) #ukuran matriks baris x kolom
A = Matriks(ukuran[0],ukuran[1])
newlist=[]
for i in range(0,ukuran[0]):
    isi = list(map(int,input()))
    for i in range(0,len(isi)):
        newlist.append(isi[i])
A.set(newlist)
trial=int(input())#banyak percobaan
for i in range(0,trial):
    coordinate = list(map(int,input().split())) # dari(b1,c1) ke (b2,c2)
    x1=coordinate[0]
    y1=coordinate[1]
    x2=coordinate[2]
    y2=coordinate[3]
    if(A.value(x1,y1)==A.value(x2,y2)):#jika nilai(b1,c1) sama dengan nilai (b2,c2)
        a_coordinate=A.find(A.value(x1,y1))#mapping semua nilai yg sama dengan nilai (b1,c1)
        res = walk(A.value(x1,y1),x1,y1,x2,y2,a_coordinate)
        if(res==1):
            print("decimal")
        elif(res==0):
            print("binary")
        elif(res==2 or res==None):
            print("neither")
    else:
        print("neither")