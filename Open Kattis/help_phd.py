iteration = int(input())
for tc in range(iteration):
  op = input()
  if(op == "P=NP"):
    print('skipped')
  else:
    num = op.split('+')
    print(int(num[0]) + int(num[1]))