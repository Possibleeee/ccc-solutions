a = int(input())
b = int(input())
temp = 0
c = 2

while a - b >= 0:
    c += 1
    temp = a
    a = b
    b = temp - b

print(c)