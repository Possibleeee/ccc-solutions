import sys

x = int(input())
m = int(input())

# for n in range(1, m):
#     o = 0
#     while m * o + 1 < x * n:
#         o += 1
#         if x * n == m * o + 1:
#             print(n)
#             sys.exit()
#
# print("No such integer exists.") # my method

for n in range(1, m):
    if (x * n) % m == 1:
        print(n)
        break
else:
    print("No such integer exists.") # teacher method