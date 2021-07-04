iter = int(input())
for trial in range(0,iter):
    l = list(map(int,input().split()))
    score = [l[4],l[5],l[6]]
    maks = 0
    maks_2 = 0
    for item in score:
        if item>maks :
            maks_2=maks
            maks=item
        elif item>maks_2:
            maks_2=item
    grade = l[0]+l[1]+l[2]+l[3]+((maks+maks_2)/2)
    if grade>=90:
        grade = "A"
    elif grade>=80:
        grade = "B"
    elif grade>=70:
        grade = "C"
    elif grade>=60:
        grade = "D"
    else:
        grade = "F"
    print("Case {}: {}".format(trial+1,grade))