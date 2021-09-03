if __name__ == '__main__':
    l = []
    N = int(input())
    for i in range(N):
        command = input()
        s = []
        s = command.split()
        if len(s) == 1:
            if s[0]=='print':
                print(l)
            elif s[0] == 'pop':
                l.pop()
            elif s[0][0]=='s':
                l.sort()
            elif s[0][0] == 'r':
                l.reverse()
        elif len(s) == 2:
            if s[0][0] == 'a':
                l.append(int(s[1]))
            elif s[0][0] == 'r':
                l.remove(int(s[1]))
        elif len(s) == 3:
            if s[0][0] == 'i':
                l.insert(int(s[1]),int(s[2]))

    