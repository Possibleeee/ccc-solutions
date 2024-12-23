a, b = input().split()
a = int(a)
b = int(b)

'''
3 30

Sun Mon Tue Wed Thr Fri Sat
          1   2   3   4   5
  6   7   8   9  10  11  12
 13  14  15  16  17  18  19
 20  21  22  23  24  25  26
 27  28  29  30
'''

print("Sun Mon Tue Wed Thr Fri Sat")
print("    " * (a - 1), end = "")
for i in range(1, b + 1):
    