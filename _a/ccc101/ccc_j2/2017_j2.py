a = int(input())
b = int(input())
new = a

for i in range(b):
    i += 1
    new = new + a * (10 ** i)

print(new)