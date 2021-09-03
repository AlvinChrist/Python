kalimat = input()
list_of_kata = kalimat.split(' ')
set_of_kata = set(list_of_kata)
if(len(list_of_kata) != len(set_of_kata)):
  print('no')
else:
  print('yes')