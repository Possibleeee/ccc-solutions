import math

tiles = int(input())
iteration = 0
sideL = 0

while sideL <= tiles:
    iteration += 1
    sideL = (iteration ** 2)

sideL = iteration - 1




print(f"The largest square has side length {sideL}.")


# Hary
ok = math.sqrt(tiles)
ans = 0
if type(ok) == int:
    ans = ok
else:
    ans = math.floor(ok)
print(f"The largest square has side length {ans}.")