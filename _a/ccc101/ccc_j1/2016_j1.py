wins = 0

for _ in range(6):
    a = input()
    if a == "W":
        wins += 1

if wins >= 5:
    print(1)
elif wins >= 3:
    print(2)
elif wins >= 1:
    print(3)
else:
    print(-1)