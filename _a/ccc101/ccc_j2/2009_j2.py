a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = 0

for i in range (d // a + 1):
    for o in range (d // b + 1):
        for p in range (d // c + 1):
            if a * i + b * o + c * p <= d:
                if not i == o == p == 0:
                    print(f"{i} Brown Trout, {o} Northern Pike, {p} Yellow Pickerel")
                    e += 1

print(f"Number of ways to catch fish: {e}")