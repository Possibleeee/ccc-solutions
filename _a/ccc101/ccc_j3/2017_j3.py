a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = int(input())

if c - (abs(a[0] - b[0]) + abs(a[1] - b[1])) < 0:
    print("N")
elif c - (abs(a[0] - b[0]) + abs(a[1] - b[1])) == 0:
    print("Y")
else:
    d = c - (abs(a[0] - b[0]) + abs(a[1] - b[1]))
    if d % 2 == 0:
        print("Y")
    else:
        print("N")