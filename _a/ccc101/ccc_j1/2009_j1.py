iteration = 0
g = 0

a = input()
b = input()
c = input()

d = "9780921418" + a + b + c

for letter in d:
    iteration += 1
    if iteration % 2 == 1:
        e = 1
    else:
        e = 3
    f = int(letter) * e
    g = g + f

print(f"The 1-3-sum is {g}")