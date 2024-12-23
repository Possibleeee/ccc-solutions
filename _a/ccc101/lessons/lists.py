# create list
from os import remove

a = []
a = ["a", "b", "c", "d"]
print(type(a))
print(a)

# read list index
print(a[1])
# a[start:stop]
print(a[1:3]) # remember this is non-inclusive
for e in a:
    print(e)

#################################################
print()
# a list can also store multiple types of data
a = ["a", "b", "3", "1"]
print(type(a))
print(a)

# read list index
print(a[1])
# a[start:stop]
print(a[1:3]) # remember this is non-inclusive
for e in a:
    print(e)

print()
# update
a.append("z")
print(a)
a.insert(0, "1")
print(a)
a[0] = 100
print(a)
a.pop(0)
print(a)
a.clear()
print(a)

# difference between a.clear() and a = []
# a = [1, 2, 3]
# b = a
# a.clear()
# print(a)  # Output: []
# print(b)  # Output: []

# a = [1, 2, 3]
# b = a
# a = []
# print(a)  # Output: []
# print(b)  # Output: [1, 2, 3]


# operations for collections (such as a list)
# create, read, update, delete, query (CRUDQ)

print()
# convert string to list
a = list("hijk")
print(a)
a.remove("i")
print(a)
# query
print(100 in a)
print(100 not in a)
print(len(a))
print(a.index("j"))

print()
a = [2, 4, 1, 5, 7]
# sorting
a.sort()
print(a)
a.extend([100, 200, 300])
print(a)
a.reverse()
print(a)

# copy and nuances
b = a[:]
c = a
print("id for a:", id(a))
print("id for b:", id(b))
# c is called an alias
print("id for c:", id(c))

print()
# how to know if copy or alias
a = [1, 2, 3]
b = a
b[0] = 100
print("b:", b)
print("a:", a)
b = a[:]
b[0] = 1000
print("b:", b)
print("a:", a)

print()
s = 'abc'
l = list(s)
print(l)

# abc
ss = ''.join(l)
print(ss)

# a b c
ss = ' '.join(l)
print(ss)
# or
# unpack
print(*l)