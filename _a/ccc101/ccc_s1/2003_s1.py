currPosition = 1
while True:
    if currPosition == 100:
        print("You Win!")
        break
    a = int(input())
    if a == 0:
        print("You Quit!")
        break
    currPosition += a
    if currPosition == 54:
        currPosition = 19
        print(f"You are now on square {currPosition}")
    elif currPosition == 90:
        currPosition = 48
        print(f"You are now on square {currPosition}")
    elif currPosition == 99:
        currPosition = 77
        print(f"You are now on square {currPosition}")
    elif currPosition == 9:
        currPosition = 34
        print(f"You are now on square {currPosition}")
    elif currPosition == 40:
        currPosition = 64
        print(f"You are now on square {currPosition}")
    elif currPosition == 67:
        currPosition = 86
        print(f"You are now on square {currPosition}")
    elif currPosition > 100:
        currPosition -= a
        print(f"You are now on square {currPosition}")
    else:
        print(f"You are now on square {currPosition}")