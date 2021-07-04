s = True
num_list = []
try:
    while s:
        num = int(input())
        num_list.append(num)
        num_list.sort()
        total = len(num_list)
        if total==1:
            print(num_list[0])
        elif total%2==0:
            median = int((num_list[int(int(total/2)-1)] + num_list[int(int(total/2))])/2)
            print(median)
        else:
            print(num_list[int(total/2)])
except EOFError or KeyboardInterrupt:
    s = False