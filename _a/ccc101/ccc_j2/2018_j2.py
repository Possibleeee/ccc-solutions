a = int(input())
b = input()
c = input()
ans = 0

for i in range(a):
    if b[i] == c[i] == 'C':
        ans += 1

print(ans)