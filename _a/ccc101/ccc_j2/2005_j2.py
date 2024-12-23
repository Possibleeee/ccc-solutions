a = int(input())
b = int(input())
c = 0
d = 0

for i in range(a, b + 1):
    if c == 4:
        d += 1
    c = 0
    for o in range(1, i + 1):
        if i % o == 0:
            c += 1

# Need one final check because the last check inside for loop doesn't execute
if c == 4:
    d += 1
print(f"The number of RSA numbers between {a} and {b} is {d}")