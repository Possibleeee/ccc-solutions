# computer cannot accurately represent
# most of the floating number
a=0.1
b=0.2
c=0.3
print(a+b==c)
print(a+b)

# why computer cannot?
# binary number system cannot represent
# the decimal number system
# for example,
# we cannot represent 1/3 by decimal number
# 0.3333333333333333.......

# how do we check if 2 floating numbers are equal
diff=(a+b)-c
if diff<1e-9:
  print('they are equal')
else:
  print('they are not equal')