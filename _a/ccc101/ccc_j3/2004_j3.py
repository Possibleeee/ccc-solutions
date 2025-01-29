a = int(input())
b = int(input())
c = [input() for _ in range(a)]
d = [input() for _ in range(b)]
for i in range(a):
    for o in range(b):
        print(f"{c[i]} as {d[o]}")