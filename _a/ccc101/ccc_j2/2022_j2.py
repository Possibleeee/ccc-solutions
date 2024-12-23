a = int(input())
d = 0

for i in range(a):
    b = int(input())
    c = int(input())
    if b * 5 - c * 3 > 40:
        d += 1

print(f"{d}+" if a == d else d)