i=int(input()) # i=3
icon=['*x*', ' xx','* *']
for line in icon:
  for time in range(i):
    for c in line:
      print(c*i,end='')
    print()