if __name__ == '__main__':
    nested_list = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        nested_list.append([score,name])
    nested_list.sort()
    tmp = nested_list[0][0]
    found = False
    for student in nested_list:
        if student[0] > tmp and not found:
            tmp = student[0]
            found = True
            print(student[1])
        elif (found and tmp == student[0]):
            print(student[1])
        elif found:
            break
            