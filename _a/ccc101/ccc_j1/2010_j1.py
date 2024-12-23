# hardcoded, see bottom
# ctrl + "/" to uncomment all after selection

# a = int(input())
#
# if a == 1:
#     print(1)
# elif a == 2:
#     print(2)
# elif a == 3:
#     print(2)
# elif a == 4:
#     print(3)
# elif a == 5:
#     print(3)
# elif a == 6:
#     print(3)
# elif a == 7:
#     print(2)
# elif a == 8:
#     print(2)
# elif a == 9:
#     print(1)
# else:
#     print(1)

# if use non hardcode, we can see in this example that,
# 4
# 4 0
# 3 1
# 2 2
# 1 3 (cant)
# basically, the left side can not go lower than half
# of its number, in this case, not < 2 (4 / 2)

a = int(input())
l = 0
r = 0
ways = 0

while l + r != a and l < 5:
    l += 1
while l >= (a / 2) and r <= l:
    if l + r != a:
        r += 1
    else:
        ways += 1
        l -= 1
        r += 1
print(ways)

# teacher's way below

# brute force: list all possible cases, and check each case to see if it is valid
# how to use counter

# a=int(input())
#
# '''
# L R
# 1 a-1
# 2 a-2
# 3 a-3
# 4 a-4
# 5 a-5
#
# '''
# count=0
# for L in range(5+1):
#   R=a-L
#   if R >= 0 and L >= R: # filter
#     # print('left:', L, 'right', R)
#     # count=count+1
#     count+=1
# print(count)