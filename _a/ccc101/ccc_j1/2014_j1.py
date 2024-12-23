a = int(input())
b = int(input())
c = int(input())

if a + b + c != 180:
    print("Error")
elif a == b == c:
    print("Equilateral")
elif a == b or b == c or a == c:
    print("Isosceles")
elif a != b != c:
    print("Scalene")

print("Error" if a + b + c != 180 else "Equilateral" if a == b == c else "Isosceles" if a == b or b == c or a == c else "Scalene" if a != b != c else exit(0))