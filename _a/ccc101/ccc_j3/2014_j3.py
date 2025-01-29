a = int(input())
antonia, david = 100, 100

for _ in range(a):
    b = input().split()
    b = [int(i) for i in b]
    if b[0] == b[1]:
        pass
    elif b[0] > b[1]:
        david -= b[0]
    else:
        antonia -= b[1]

print(antonia, david, sep="\n")