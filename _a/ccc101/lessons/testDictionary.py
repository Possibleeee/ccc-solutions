l = [1, 2, 3]
print(l[1], end= "\n\n")

# no index, no duplicate, no order
s = set() # empty set
s = {1, 2, 3}

# map == dictionary
# dictionary is a collection of key-value pairs
# no duplicate, has order
d = {} # empty dictionary
d = {
    # key:value
    1 : 100,
    2 : 200,
    3 : 300
}

# create, read, update, delete, query (CRUDQ)

print(d[2]) # read
d[2] = "saturday" # update
d[5] = 500 # insert
print(d)

d.pop(5) # delete

print(d)
print(len(d))
d.clear()
print(d)

print(1 in d) # query
d[1] = 100
print(1 in d)
print(100 in d) # works for keys, not values