a = list(map(int, input().split()))

for i in range(5):
    for o in range(5):
        if i > o:
            print(sum(a[o:i]), end= " ")
        else:
            print(sum(a[i:o]), end= " ")
    print()