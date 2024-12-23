P = int(input())
N = int(input())
R = int(input())
days = 0
_ = N

while not P < N:
    _ = _ * R
    N += _
    days += 1

print(days)