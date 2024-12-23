a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
c = [int(i) for i in input().split()]
d = [int(i) for i in input().split()]

# print(a[0] + a[1] + a[2] + a[3])
# print(b[0] + b[1] + b[2] + b[3])
# print(c[0] + c[1] + c[2] + c[3])
# print(d[0] + d[1] + d[2] + d[3])
# print(a[0] + b[0] + c[0] + d[0])
# print(a[1] + b[1] + c[1] + d[1])
# print(a[2] + b[2] + c[2] + d[2])
# print(a[3] + b[3] + c[3] + d[3])

if a[0] + a[1] + a[2] + a[3] == b[0] + b[1] + b[2] + b[3] == c[0] + c[1] + c[2] + c[3] == d[0] + d[1] + d[2] + d[3] == a[0] + b[0] + c[0] + d[0] == a[1] + b[1] + c[1] + d[1] == a[2] + b[2] + c[2] + d[2] == a[3] + b[3] + c[3] + d[3]:
    print("magic")
else:
    print("not magic")