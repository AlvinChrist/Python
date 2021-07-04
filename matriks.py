import numpy as np
from copy import deepcopy
class Matriks:
    def __init__(self,baris,kolom):
        self.baris = baris
        self.kolom = kolom
        self.matriks = [['' for i in range(0,kolom)] for j in range(0,baris)]
        self.error = False
        self.persegi=False
        if(baris==kolom):
            self.persegi=True
    
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
        else:
            print("Total data harus {}!".format(self.baris*self.kolom)) #jika total data matriks tidak sama  
            self.error = True                                           #dengan ukuran matriks, munculkan error    

    def showall(self): #menampilkan seluruh matriks
        if not self.error:
            for n in range(0,len(self.matriks)):
                print(self.matriks[n])
        
    def value(self,b,k): #return data matriks baris ke b dan kolom ke k
        if not self.error:
            return self.matriks[b-1][k-1]
    
    def find(self,value): #mencari letak satu nilai spesifik pada matriks
        if not self.error:
            coordinate_map=[]
            for b in range(1,self.baris+1):
                for k in range(1,self.kolom+1):
                    if(A.value(b,k)==value):
                        coordinate_map.append([b,k])
            return coordinate_map
        
    def determinan(self): #mencari determinan metode kofaktor
        if (not self.error)and(self.persegi): #syarat determinan: harus merupakan matriks persegi
            if not self.find(0):
                b=0
            else:
                b=self.find(0)[0]-1
            det=0
            for k in range(0,self.kolom):
                kofaktor=(-1)**(b+k)*self.matriks[b][k]
                m_minor = np.delete(np.delete(self.matriks,b,axis=0),k,axis=1) #membuat matriks minor
                minor_determinan=round(np.linalg.det(m_minor))#mencari determinan matriks minor
                det+=kofaktor*minor_determinan#kofaktor*determinan minor
            return det
        else:
            return("Matriks harus matriks persegi!")

    def invers(self):
        if (not self.error)and(self.persegi): #syarat invers: harus merupakan matriks persegi dengan determinan bukan 0
            if(self.determinan()!=0):
                n_matrix=np.asmatrix(self.matriks)
                inv=(1/self.determinan())*n_matrix.getH()
                return inv
            else:
                return False
        else:
            return False
     
    def transpose(self):
        n_matrix=np.asmatrix(self.matriks)
        return n_matrix.transpose()
    
    def is_orthogonal(self): #memeriksa apakah matriks merupakan matriks orthogonal
        if(self.persegi):
            C=np.array(self.matriks)
            C_T=np.array(self.transpose().tolist())
            I=np.identity(self.baris)
            if((np.matrix.round(C_T.dot(C),5)==I).all()):
                return True
        else:
            return False

    
    def GramSchmidt(self):
        m_T = self.transpose().tolist() #membalik kolom->baris untuk memudahkan indexing
        u1 = np.array(m_T[0])
        u2 = np.array(m_T[1])
        u3 = np.array(m_T[2])
        
        V1 = u1

        norm_v1 = np.linalg.norm(V1)
        u2_v1 = np.dot(u2,V1)
        V2 = u2 - (((u2_v1)/(norm_v1**2))*V1)
    
        norm_v2 = np.linalg.norm(V2)
        u3_v1 = np.dot(u3,V1)
        u3_v2 = np.dot(u3,V2)
        V3    = u3 - (((u3_v1)/(norm_v1**2))*V1) - (((u3_v2)/(norm_v2**2))*V2)
        if V3.any==0:
            w3=0
        norm_v3 = np.linalg.norm(V3)
        w1 = V1/(norm_v1) #menghitung vektor orthonormal
        w2 = V2/(norm_v2)
        w3 = V3/(norm_v3)
        
        m_T[0]=w1.tolist() #membuktikan bahwa proses Gram-Schmidt menghasilkan matriks orthogonal
        m_T[1]=w2.tolist()
        m_T[2]=w3.tolist()
        flat_m_T = [x for sublist in m_T for x in sublist]
        C = Matriks(3,3)
        C.set(flat_m_T)
        C.matriks = C.transpose()
        print("Vektor-vektor kolom ortonormal yang diperoleh dari proses Gram-Schmidt adalah:")
        print("Vektor kolom 1 : {}\nVektor kolom 2 : {}\nVektor kolom 3 : {}\n".format(w1,w2,w3))
        print("#########################")
        print("Pembuktian")
        print("#########################")
        print("Matriks baru yaitu matriks C dengan vektor kolom di atas")
        for a in C.matriks:
            print(a)
        print("\nApakah Matriks C orthogonal : {}".format(C.is_orthogonal())) 
        
        
"""Cara mengisi nilai matriks
   Misal : A = Matriks (3x3)
           A.set([1,2,3,4,5,6,7,8,9])
                                      [1,2,3]
           maka matriksnya menjadi A =[4,5,6]
                                      [7,8,9]
 """
def cramer(A,B,kolom): #menggunakan metode cramer dan substitusi kolom ke n dengan vektor hasil
    if(A.determinan()!=0):
        if(A.baris==B.baris):
            mA = deepcopy(A)
            mB = deepcopy(B)
            k=kolom-1
            for b in range(0,mB.baris):
                mA.matriks[b][k]=mB.matriks[b][0]
            res = mA.determinan()/A.determinan()
            return mA.matriks,res #kembalikan matriks , nilai dari |Ax|/|A|
        else:
            print("Salah satu matriks harus matriks persegi!\n")
            return False
    else:
        print("Tidak ada solusi SPL karena Determinan A=0\n")
        return False
        
A = Matriks(3,3) #matriks ordo 3x3
B = Matriks(3,1) #vektor 3x1

A.set([0,2,3,-2,5,2,-4,2,7])
B.set([6,14,-2])
print("Matriks A ")
A.showall()
print('\n')
print("Matriks B ")
B.showall()
print('\n')

print('-------------')
print("Nomor 1")
print('-------------')
print("Determinan matriks A= "+str(A.determinan()))
print("Determinan matriks B= "+str(B.determinan()))
print('\n')

print('-------------')
print("Nomor 2")
print('-------------')
print("Invers matriks A")
if(A.persegi):
    if(A.determinan()!=0):
        print(A.invers())
    else:
        print("Tidak ada invers karena Determinan=0")
else:
    print("Matriks A bukan matriks persegi")
print('\n')
print("Invers matriks B")
if(B.persegi):
    if(B.determinan()!=0):
        print(B.invers())
    else:
        print("Tidak ada invers karena Determinan=0")
else:
    print("Matriks B bukan matriks persegi")
print('\n')

print('-------------')
print("Nomor 3")
print('-------------')
if(cramer(A,B,1)):
    print("Penyelesaian SPL (anggap matriks A adalah koefisien sebuah SPL dengan penyelesaian x,y,z)")
    print("x = |Ax|/|A|")
    print("Matriks Ax")
    for v in cramer(A,B,1)[0]:
        print("    {}".format(v))
    print("---------------- :")
    print("Matriks A")
    for v in A.matriks:
        print("    {}".format(v))
    print("x = {}\n".format(cramer(A,B,1)[1])) #cramer(A,B,1) -> menghitung nilai x dengan substitusi vektor hasil B pada kolom 1 matriks A
    
    print("y = |Ay|/|A|")
    print("Matriks Ay")
    for v in cramer(A,B,2)[0]: #cramer(A,B,2) -> menghitung nilai y dengan substitusi vektor hasil B pada kolom 2 matriks A
        print("    {}".format(v))
    print("---------------- :")
    print("Matriks A")
    for v in A.matriks:
        print("    {}".format(v))
    print("y = {}\n".format(cramer(A,B,2)[1]))
    
    print("z = |Az|/|A|")
    print("Matriks Az")
    for v in cramer(A,B,3)[0]:
        print("    {}".format(v))
    print("---------------- :")
    print("Matriks A")
    for v in A.matriks:
        print("    {}".format(v))
    print("z = {}\n".format(cramer(A,B,3)[1])) #cramer(A,B,3) -> menghitung nilai x dengan substitusi vektor hasil B pada kolom 3 matriks A
    if(cramer(A,B,1)[1]==0)and(cramer(A,B,2)[1]==0)and(cramer(A,B,3)[1]==0):
        print("SPL mempunyai solusi trivial")
    else:
        print("Maka penyelesaian SPL = x={}, y={}, z={}\n".format(cramer(A,B,1)[1],cramer(A,B,2)[1],cramer(A,B,3)[1]))

print('-------------')
print('Nomor 4')
print('-------------')
if(A.is_orthogonal()):
    print("Matriks A adalah matriks orthogonal")
else:
    print("Matriks A bukan matriks orthogonal")
if(B.is_orthogonal()):
    print("Matriks B adalah matriks orthogonal")
else:
    print("Matriks B bukan matriks orthogonal\n")
    
print('-------------')
print('Nomor 5')
print('-------------')
print("Matriks A")
if(A.determinan()==0):
    print("Matriks A bukan merupakan matriks orthonormal")
else:
    A.GramSchmidt()