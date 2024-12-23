# Reminder on how to find the LCM (Least Common Multiple)
#
# First, find the prime factors of 2, 3, 4, 5
#
# 2^1 (2, on a theoretical paper, cross this out)
# 3^1 (3)
# 2^2 (4)
# 5^1 (5)
#
# To find LCM, we need the highest power of each prime factor.
#
# In this case, the highest power of,
#
# 2 is 2, between 2^1 and 2^2
# 3 is 1, between 3^1 and nothing
# 4 is 1, between 4^1 and nothing
# 5 is 1, between 5^1 and nothing
#
# Now to find LCM,
# 3^1 * 2^2 * 5^1 = 60
#
# Therefore the LCM of 2, 3, 4, 5, is 60

#############################################################################

# Example: Find the LCM of 12, 18, and 30
#
# Step 1: Find the prime factors
# Let’s break each number down into its prime factors:
# 12 = 22 × 3112 = 2^2 * 3^112 = 22×31
# 18 = 21 × 3218 = 2^1 * 3^218 = 21×32
# 30 = 21 × 31 × 5130 = 2^1 * 3^1 * 5^130=21×31×51
#
# Step 2: Identify the highest power of each prime factor
# To find the LCM, we take the highest power of each prime factor present in any of the numbers:
# For 2, the highest power is 2^2 (from 12).
# For 3, the highest power is 3^2 (from 18).
# For 5, the highest power is 5^1 (from 30).
#
# Step 3: Multiply these highest powers to get the LCM
#
# Now, we combine these highest powers:
# LCM = 2^2 × 3^2 × 5^1
# Calculating step-by-step:
# 2^2 = 4
# 3^2 = 9
# 5^1 = 5
#
# Then,
# 4 × 9 × 5 = 180
#
# Conclusion
# The LCM of 12, 18, and 30 is 180.

############################################################################

# As for solving this problem, we can hard-code in the LCM of 60 in line 65

a = int(input())
b = int(input())

print(f"All positions change in year {a}")

while True:
    if a + 60 <= b:
        a += 60
        print(f"All positions change in year {a}")
    else:
        break # 69 lines, nice!