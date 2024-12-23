a = int(input())
for i in range(0, a):
    sentence = input().split()
    for word in sentence:
        if len(word) == 4:
            print("****", end= " ")
        else:
            print(word, end= " ")
    print()