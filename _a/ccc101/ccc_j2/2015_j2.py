a = input()
b = a.count(":-)")
c = a.count(":-(")

if b == c == 0:
    print("none")
elif b == c:
    print("unsure")
elif b > c:
    print("happy")
else:
    print("sad")