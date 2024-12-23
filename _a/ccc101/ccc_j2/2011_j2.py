# h = int(input())
# M = int(input())

# for t in range(M):
#     t += 1
#     A = -6 * t ** 4 + h * t ** 3 + 2 * t ** 2 + t
#     if A <= 0:
#         print(f"The balloon first touches ground at hour:\n{t}")
#         break
# if A > 0:
#     print("The balloon does not touch ground in the given time.")
#########################################
# h = int(input())
# M = int(input())
# t = 0
# A = 1
#
# while t <= M and A > 0:
#     t += 1
#     A = -6 * t ** 4 + h * t ** 3 + 2 * t ** 2 + t
#     if A <= 0:
#         print(f"The balloon first touches ground at hour:\n{t}")
# if A > 0:
#     print("The balloon does not touch ground in the given time.")

# why dont this sh workkk
#########################################
# h = int(input())
# M = int(input())
# t = 0
# A = 1

# while True:
#     t += 1
#     if t > M:
#         print("The balloon does not touch ground in the given time.")
#         break
#     A = -6 * t ** 4 + h * t ** 3 + 2 * t ** 2 + t
#     if A <= 0:
#         print(f"The balloon first touches ground at hour:\n{t}")
#         break