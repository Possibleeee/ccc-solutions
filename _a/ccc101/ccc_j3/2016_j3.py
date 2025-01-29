a = input()
b = ""

for i in range(len(a)):
    for o in range(i + 1, len(a) + 1):
        if a[i:o] == a[i:o][::-1]:
            if len(a[i:o]) > len(b):
                b = a[i:o]
print(len(b))