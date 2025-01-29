# a is number of test cases
# b contains number of chests, and goal value
# c contains values of each chest
# d tracks how many coins taken
# e contains value of last chest taken

a = int(input()) # test cases

# line 12 - 14 gets input
for _ in range(a):
    d = 0  # don't care
    b = [int(x) for x in input().split()]
    c = [int(x) for x in input().split()]
    c.sort(reverse= True)
    if c[0] == b[1]: # check if we need to do anything
        print(0)
    else: # aww, man we need to do something
        while d < b[1]: # checks if goal reached or surpassed
            if not c:
                break
            e = c.pop(0)
            d += e
        if d == b[1]: # check if we need to do anything (could be combination of most coin chests, so not duplicate)
            print(0)
        else: # aww, man we need to do something
            if d < b[1]: # are we below goal? (aka ran out of chests)
                print(abs(b[1] - d))
            else: # bro took too much, this greedy little mf
                d -= e
                print(abs(b[1] - d))