import math

def rounds(n):
    if n - int(n) == 0.5:
        return int(n) + 1
    else:
        return round(n)

'''
Test cases:
60
100
23
1
64507
'''

a = 1
while a != 0:
    a = int(input())
    if a == 0:
        break
    b = math.sqrt(a)
    c = b

    if b * c == a and b.is_integer():
        b = int(b)
        c = int(c)
        print(f"Minimum perimeter is {(b + c) * 2} with dimensions {c} x {b}")
    else:
        b = rounds(b)
        c = b
        while b * c > 0:
            b += 1
            if b * c == a:
                print(f"Minimum perimeter is {(b + c) * 2} with dimensions {c} x {b}")
                break
            c -= 1
            if b * c == a:
                print(f"Minimum perimeter is {(b + c) * 2} with dimensions {c} x {b}")
                break
        else:
            print(f"Minimum perimeter is {(1 + a) * 2} with dimensions 1 x {a}")