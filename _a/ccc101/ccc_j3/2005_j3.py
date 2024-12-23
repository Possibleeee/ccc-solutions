'''
R
QUEEN
R
FOURTH
R
SCHOOL

Turn LEFT onto FOURTH street.
Turn LEFT onto QUEEN street.
Turn LEFT into your HOME.

'''

path=[]
while True:
  a=input()
  if a=='SCHOOL':
    break
  # print(a)
  path.append(a)

for i in range(len(path)):
  if path[i]=='R':
    path[i]='LEFT'
  elif path[i]=='L':
    path[i]='RIGHT'

path=path[::-1]
path.append('HOME')
# print(path)

for i in range(len(path)//2):
  if path[2*i+1]=='HOME':
    print('Turn',path[2*i],'into your HOME.')
  else:
    print('Turn',path[2*i],'onto',path[2*i+1],'street.')