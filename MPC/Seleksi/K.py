if __name__ == '__main__':
    while True:
        try:
            A = list(map(str,input().split(" ")))
            B = []
            for itm in A:
                B.append(itm[::-1])
            print(*B)
        except:
            break