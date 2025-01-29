quarters = int(input())
machine1 = int(input()) # +30 everu 35
machine2 = int(input()) # +60 every 100
machine3 = int(input()) # +9 every 10

machine_number = 0
counter = 0
while quarters != 0:
    quarters -= 1
    counter += 1
    machine_number += 1
    if machine_number % 3 == 1:
        machine1 += 1
        if machine1 % 35 == 0:
            quarters += 30
    elif machine_number % 3 == 2:
        machine2 += 1
        if machine2 % 100 == 0:
            quarters += 60
    else:
        machine3 += 1
        if machine3 % 10 == 0:
            quarters += 9

print(f"Martha plays {counter} times before going broke.")