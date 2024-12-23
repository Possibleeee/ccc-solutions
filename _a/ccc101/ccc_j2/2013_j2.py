# a = input()
# print("YES" if "A" not in a and "B" not in a and "C" not in a and "D" not in a and "E" not in a and "F" not in a and "G" not in a and "J" not in a and "K" not in a and "L" not in a and "M" not in a and "P" not in a and "Q" not in a and "R" not in a and "T" not in a and "U" not in a and "V" not in a and "W" not in a and "Y" not in a else "NO")

a = input()
for i in a:
    if i not in "IOSHZXN":
        print("NO")
        break
else:
    print("YES")

# In Python, the variable i in a for loop takes on the type of the elements in the iterable you are looping over. Here’s how it works:
#
# If you loop over a string, i will be a character (string of length 1).
# If you loop over a list, i will be each element of the list.
# If you loop over a range, i will be an integer.
# Here are some examples to illustrate:
#
# Looping over a string:
# Python
#
# a = "hello"
# for i in a:
#     print(i)  # i is a character (string of length 1)
# AI-generated code. Review and use carefully. More info on FAQ.
# Looping over a list:
# Python
#
# a = [1, 2, 3, 4, 5]
# for i in a:
#     print(i)  # i is an element of the list (integer in this case)
# AI-generated code. Review and use carefully. More info on FAQ.
# Looping over a range:
# Python
#
# for i in range(5):
#     print(i)  # i is an integer
# AI-generated code. Review and use carefully. More info on FAQ.
# So, i will be a string if you are looping over a string, and it will be an integer if you are looping over a range. The type of i depends on the type of the elements in the iterable you are iterating over.