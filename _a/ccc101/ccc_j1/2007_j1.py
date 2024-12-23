l = [0, 0, 0]

for i in range(len(l)):
    l[i] = int(input())

while True: 
    for i in range(len(l)-1):
        sort = 0
        if l[i] > l[i+1]:
            l[i], l[i+1] = l[i+1], l[i]
            sort = 1
        elif sort != 1:
            sort = 0
    if sort == 0:
        break
print(l[1])