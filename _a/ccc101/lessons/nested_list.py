l = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# lists in a list

print(l[2][1]) # prints index 1 at list index 2

print()
for row in l:
    print(row) # print all rows

print()
for row in l:
    for i in row:
        print(i) # print all values

# 2 loops up here doesn't give you the index
# the loop down here does give you the index

print()
for i in range(len(l)): # note how we are using len() instead of range()
    print(f"row index: {i}")
    print(l[i])
    for o in range(len(l[i])):
        print(f"column index: {o}")
        print(l[i][o])

print()
a = [ [1] , [2,3] , [4,5,6] , [7,8] , [9] ]

# 1
# 2 3
# 4 5 6
# 7 8
# 9

for row in a:
    for i in row:
        print(i, end= " ") # end= customizes the ending character
        print()            # by default is newline
        