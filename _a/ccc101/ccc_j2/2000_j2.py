a = int(input())
b = int(input())
c = 0

for i in range(a, b + 1):
    d = 0
    i = str(i)

    for index in range(len(i)):
        if i[index] in "01869":
            if i[index] == i[-(index + 1)] and i[index] not in "69" \
                    or i[index] == "6" and i[-(index + 1)] == "9" \
                    or i[index] == "9" and i[-(index + 1)] == "6":
                d += 1
        else:
            break
    else:
        if d == len(i):
            c += 1

print(c)