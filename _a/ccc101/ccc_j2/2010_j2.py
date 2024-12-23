a = int(input())
b = int(input())
c = int(input())
d = int(input())

e = int(input())

Nikky = 0
Byron = 0

# Nikky distance calc
i = 0
while i < e:
    for _ in range(a):
        if i == e:
            break
        Nikky += 1
        i += 1
    for _ in range(b):
        if i == e:
            break
        Nikky -= 1
        i += 1

# Byron distance calc
i = 0
while i < e:
    for _ in range(c):
        if i == e:
            break
        Byron += 1
        i += 1
    for _ in range(d):
        if i == e:
            break
        Byron -= 1
        i += 1

# Who wins
if Nikky == Byron:
    print("Tied")
elif Nikky > Byron:
    print("Nikky")
else:
    print("Byron")

# You
# Sent by you:
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
#
# e = int(input())
#
# Nikky = 0
# Byron = 0
#
# # Nikky distance calc
# i = 0
# while True:
#     for _ in range(a):
#         if i == e:
#             break
#         Nikky += 1
#         i += 1
#     for _ in range(b):
#         if i == e:
#             break
#         Nikky -= 1
#         i += 1
#     if i == e:
#         break
#
# # Byron distance calc
# i = 0
# while True:
#     for _ in range(c):
#         if i == e:
#             break
#         Byron += 1
#         i += 1
#     for _ in range(d):
#         if i == e:
#             break
#         Byron -= 1
#         i += 1
#     if i == e:
#         break
#
# # Who wins
# if Nikky == Byron:
#     print("Tied")
# elif Nikky > Byron:
#     print("Nikky")
# else:
#     print("Byron")
#
#
#
# Copilot
# Using
# the web
# Sent by Copilot:
# It looks like you’re working on a program to determine the winner between Nikky and Byron based on their respective movement patterns. Here’s a more concise version of your code:
#
# Python
#
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# e = int(input())
#
# Nikky = 0
# Byron = 0
#
# # Nikky distance calc
# i = 0
# while i < e:
#     for _ in range(a):
#         if i == e:
#             break
#         Nikky += 1
#         i += 1
#     for _ in range(b):
#         if i == e:
#             break
#         Nikky -= 1
#         i += 1
#
# # Byron distance calc
# i = 0
# while i < e:
#     for _ in range(c):
#         if i == e:
#             break
#         Byron += 1
#         i += 1
#     for _ in range(d):
#         if i == e:
#             break
#         Byron -= 1
#         i += 1
#
# # Who wins
# if Nikky == Byron:
#     print("Tied")
# elif Nikky > Byron:
#     print("Nikky")
# else:
#     print("Byron")
# AI-generated code. Review and use carefully. More info on FAQ.
# This version should work the same way as your original code but is a bit more streamlined. Let me know if you need any further assistance!
#
# You
# Sent by you:
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
#
# e = int(input())
#
# Nikky = 0
# Byron = 0
#
# # Nikky distance calc
# i = 0
# while i < e:
#     for _ in range(a):
#         if i == e:
#             break
#         Nikky += 1
#         i += 1
#     for _ in range(b):
#         if i == e:
#             break
#         Nikky -= 1
#         i += 1
#
# # Byron distance calc
# i = 0
# while i < e:
#     for _ in range(c):
#         if i == e:
#             break
#         Byron += 1
#         i += 1
#     for _ in range(d):
#         if i == e:
#             break
#         Byron -= 1
#         i += 1
#
# # Who wins
# if Nikky == Byron:
#     print("Tied")
# elif Nikky > Byron:
#     print("Nikky")
# else:
#     print("Byron")
# Copilot
# Using
# the web
# Sent by Copilot:
# Your updated code looks great! It should work as intended to determine the winner between Nikky and Byron based on their movement patterns. If you have any specific questions or need further assistance, feel free to ask! 😊
#
# You
# Sent by you:
# How can I make the code more efficient?
# Copilot
# Using
# the web
# Sent by Copilot:
# To make your code more efficient, you can reduce redundancy and avoid repeated loops. Here’s an optimized version of your code:
#
# Python
#
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# e = int(input())
#
# def calculate_distance(forward, backward, steps):
#     cycle_length = forward + backward
#     full_cycles = steps // cycle_length
#     remaining_steps = steps % cycle_length
#
#     distance = full_cycles * (forward - backward)
#     distance += min(remaining_steps, forward)
#     distance -= max(0, remaining_steps - forward)
#
#     return distance
#
# Nikky = calculate_distance(a, b, e)
# Byron = calculate_distance(c, d, e)
#
# if Nikky == Byron:
#     print("Tied")
# elif Nikky > Byron:
#     print("Nikky")
# else:
#     print("Byron")
# AI-generated code. Review and use carefully. More info on FAQ.
# This version uses a function to calculate the distance for both Nikky and Byron, reducing the need for repeated code and making it more efficient. Let me know if you have any questions or need further assistance! 😊
#
# You
# Sent by you:
# explain this code to me
# Copilot
# Using
# the web
# Sent by Copilot:
# Sure! Let’s break down the optimized code step by step:
#
# Python
#
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# e = int(input())
# AI-generated code. Review and use carefully. More info on FAQ.
# These lines take input values for the variables a, b, c, d, and e. These represent the forward and backward steps for Nikky and Byron, and the total number of steps e.
#
# Python
#
# def calculate_distance(forward, backward, steps):
#     cycle_length = forward + backward
#     full_cycles = steps // cycle_length
#     remaining_steps = steps % cycle_length
#
#     distance = full_cycles * (forward - backward)
#     distance += min(remaining_steps, forward)
#     distance -= max(0, remaining_steps - forward)
#
#     return distance
# AI-generated code. Review and use carefully. More info on FAQ.
# This function calculates the total distance traveled by either Nikky or Byron. Here’s how it works:
#
# cycle_length: The total number of steps in one complete cycle (forward + backward).
# full_cycles: The number of complete cycles that fit into the total steps e.
# remaining_steps: The number of steps left after accounting for the full cycles.
# distance: The total distance traveled. It starts with the distance covered in the full cycles (full_cycles * (forward - backward)), then adds the distance covered in the remaining steps. The min and max functions ensure that the distance is calculated correctly based on the remaining steps.
# Python
#
# Nikky = calculate_distance(a, b, e)
# Byron = calculate_distance(c, d, e)
# AI-generated code. Review and use carefully. More info on FAQ.
# These lines call the calculate_distance function for both Nikky and Byron, using their respective forward and backward steps and the total number of steps e.
#
# Python
#
# if Nikky == Byron:
#     print("Tied")
# elif Nikky > Byron:
#     print("Nikky")
# else:
#     print("Byron")
# AI-generated code. Review and use carefully. More info on FAQ.
# Finally, this part of the code compares the distances traveled by Nikky and Byron and prints the result:
#
# If the distances are equal, it prints “Tied”.
# If Nikky’s distance is greater, it prints “Nikky”.
# If Byron’s distance is greater, it prints “Byron”.
# I hope this helps! If you have any more questions or need further clarification, feel free to ask. 😊
