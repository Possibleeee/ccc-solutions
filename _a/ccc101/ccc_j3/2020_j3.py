a = int(input())
c = [-1, -1] # smallest number possible to ensure biggest result
d = [101, 101] # biggest number possible to ensure smallest result

for _ in range(a):
    b = list(map(int, input().split(",")))
    if b[0] > c[0]:
        c[0] = b[0]
    if b[1] > c[1]:
        c[1] = b[1]
    if b[0] < d[0]:
        d[0] = b[0]
    if b[1] < d[1]:
        d[1] = b[1]

d = [x - 1 for x in d]
c = [x + 1 for x in c]

print(f'{d[0]},{d[1]}') # smallest
print(f'{c[0]},{c[1]}') # biggest