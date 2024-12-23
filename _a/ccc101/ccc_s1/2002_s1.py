a = int(input())
b = int(input())
c = int(input())
d = int(input())
total = int(input())
count = 0
minTicket = total

'''
1
2
3
4
3

# of PINK is 0 # of GREEN is 0 # of RED is 1 # of ORANGE is 0
# of PINK is 1 # of GREEN is 1 # of RED is 0 # of ORANGE is 0
# of PINK is 3 # of GREEN is 0 # of RED is 0 # of ORANGE is 0
Total combinations is 3.
Minimum number of tickets to print is 1.
'''

for q in range(total // a + 1):
    for w in range(total // b + 1):
        for e in range(total // c + 1):
            for r in range(total // d + 1):
                if a * q + b * w + c * e + d * r == total:
                    print(f"# of PINK is {q} # of GREEN is {w} # of RED is {e} # of ORANGE is {r}")
                    count += 1
                    tickets = q + w + e + r
                    if tickets < minTicket:
                        minTicket = tickets

print("Total combinations is " + str(count) + ".")
print("Minimum number of tickets to print is " + str(minTicket) + ".")