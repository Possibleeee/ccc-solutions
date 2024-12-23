a = int(input())
b = 0
while a > b:
    b = int(input())
    if a > b:
        a += b
print(a)