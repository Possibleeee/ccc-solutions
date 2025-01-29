# while True:
a = int(input())

while True:
    lazySolution = set()
    c = 0
    a += 1
    for i in str(a):
        lazySolution.add(i)
        c += 1
    if len(lazySolution) == c:
        print(a)
        break