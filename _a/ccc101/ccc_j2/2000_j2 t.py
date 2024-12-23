'''
1
100

6
'''
a=int(input())
b=int(input())
cnt=0
for num in range(a,b+1):
  # 1
  # how to check if num includes valid digits
  valid=True
  for d in str(num):
    if d in '23457':
      valid=False
      break
  if not valid:
    continue
  # 2 simulate rotate
  '''
  include 2 steps
  1 replace 6 to 9, replace 9 to 6
  2 reverse the num
  '''
  # 10 -> 01
  # 60 -> 90 -> 09
  # 66 -> 99 -> 99
  # 69 -> 96 -> 69
  # 1616 -> 1919 -> 9191
  # 6891 -> 9861 -> 1689
  # 1661 -> 1991 -> 1991
  # 1691 -> 1961 -> 1691
  # 1691 -> 1a91 -> 1a61 -> 1961

  # step 1: replace 6 to 9, 9 to 6
  # num=69
  # print('num is', num)
  num1=str(num).replace('6','a')
  # print('after replace 6 to a', num1)
  num2=num1.replace('9','6')
  # print('after replace 9 to 6',num2)
  num3=num2.replace('a','9')
  # print('after replace a to 9',num3)

  # step 2: reverse num
  num4=num3[::-1]

  # compare the num4 with original num
  if num4==str(num):
    cnt+=1
    # print(num)
print(cnt)