e = ["A", "B", "C", "D", "E"]

while True:
    f = int(input())
    if f == 1:
        for _ in range(int(input())):
            e.append(e[0])
            del e[0]
    elif f == 2:
        for _ in range(int(input())):
            e.insert(0, e[len(e) - 1])
            del e[len(e) - 1]
    elif f == 3:
        for _ in range(int(input())):
            e[0] , e[1] = e[1] , e[0]
    else:
        print(*e)
        break