a3 = int(input()) * 3
a2 = int(input()) * 2
a1 = int(input()) * 1
b3 = int(input()) * 3
b2 = int(input()) * 2
b1 = int(input()) * 1

if a3 + a2 + a1 > b3 + b2 + b1:
    print("A")
elif a3 + a2 + a1 < b3 + b2 + b1:
    print("B")
else:
    print("T")