s = {1, 2, 3} # creates a set

# read
# set has no index
# print(s[0]) wont work

for e in s:
    print(e)

# update by add
s.add(100)
print(s)
s.add(100)
print(s) # still prints same result
         # because sets don't allow duplicates
s.add("a")
s.add("b")
s.add("c")
print(s) # n order, try rerunning code to see
print(len(s))

s.remove(1)
print(s)
e = s.pop() # no order, so random pop
print(e)
print(s)
s.add(1)
print(s)
