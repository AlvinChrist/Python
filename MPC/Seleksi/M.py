iter = int(input())
for x in range(0,iter):
    word = input()
    if(len(word)>10):
        print("{}{}{}".format(word[0],str(len(word)-2),word[len(word)-1]))
    else:
        print(word)