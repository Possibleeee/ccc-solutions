import math

a = float(input())
aT = int(math.ceil(a / 2))
aB = int(math.floor(a / 2))

for i in range(aT):
    print(f"*{'*' * (i * 2)}{' ' * int((a * 2) - ((i * 2) + (i * 2) + 2))}{'*' * (i * 2)}*")
for i in range(aB):
    i = aB - 1 - i
    print(f"*{'*' * (i * 2)}{' ' * int((a * 2) - ((i * 2) + (i * 2) + 2))}{'*' * (i * 2)}*")