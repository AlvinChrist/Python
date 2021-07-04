N = int(input("Masukkan nilai N : "))
word = input("Masukkan string : ")
keyword = "tuan"
key = [x for x in range(0,N)]
count=0
for chr in keyword:
    for _chr in word:
        if chr==_chr:
            count+=1
    key.append(count)
    count = 0

print(key)