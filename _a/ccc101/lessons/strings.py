a = 'abc'
b = 'def'

# connect 2 strings
c = a + b
print(c)

# format long strings
d = 'abc' \
    'def' \
    'ghi'
print(d)

# multiline string
a = '''
    *
*       *
    *
    '''
print(a)

print('  *')
print('*   *')
print('  *\n')

# split a string
s = '100 200'
r = s.split() # or a, b = s.split(), which would set a, b to 100, 200
print(r)
a = r[0]
b = r[1]
print(a + b)
a = int(a)
b = int(b)
print(a + b)

# replace
print()
s = "today is a bad day"
print("before replace:", s)
s.replace("bad", "good")
print("after replace:", s)
s = s.replace("bad", "good")
print("after replace:", s)

# count thingy
print()
s = "aa bbb cccc"
r = s.count("a")
print(r)

# check
print()
print("100" .isnumeric()) # is numeric string?
print("abc".isalpha()) # is alphabetic string?
print("abbc".find("b")) # find first instance of
print("abbc".find("b")) # but return -1 on failure
print("abc".zfill(10)) # z is for zero

s = "study.py"

print(s.endswith("py")) # self-explanatory
print(s.startswith("ab")) # self-explanatory
print(s.upper()) # everything capitalized
print(s.lower()) # everything un-capitalized
print("a" in s) # is "a" in var s?

#
print()
s = ["1", "4", "9", "100"]
print(" ".join(s)) # use space to join elements in s

# repeat string
print()
print("a" * 2)
print()

# reverse
s = "abc"
a = s[::-1]
a = s[-1:-0:-1]
print(a)

print()
s = "abcdefghijklmn"
# s[start:stop:step]
print(s[0::3])
print(s[::3])
print(s[-1:-15:-1])