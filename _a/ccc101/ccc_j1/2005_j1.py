d = int(input())
e = int(input())
w = int(input())

if d - 100 < 0:
    a = "%0.2f" % (0.15 * e + 0.2 * w)
else:
    a = "%0.2f" % ((d - 100) * 0.25 + 0.15 * e + 0.2 * w)
print(f"Plan A costs {a}")

if d - 250 < 0:
    b = "%0.2f" % (0.35 * e + 0.25 * w)
else:
    b = "%0.2f" % ((d - 250) * 0.45 + 0.35 * e + 0.25 * w)
print(f"Plan B costs {b}")

if a < b:
    print("Plan A is cheapest.")
elif b < a:
    print("Plan B is cheapest.")
else:
    print("Plan A and B are the same price.")