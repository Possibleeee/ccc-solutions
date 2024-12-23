a = int(input())
b = int(input())
c = 0

for i in range(a):
    for o in range(b):
        if (i + 1) + (o + 1) == 10:
            c += 1

print(f"There is {c} way to get the sum 10." if c == 1 else f"There are {c} ways to get the sum 10.")