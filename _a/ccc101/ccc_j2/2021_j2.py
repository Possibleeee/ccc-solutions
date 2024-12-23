ppl = int(input())
best = 0

for _ in range(ppl):
    name = input()
    bidding = int(input())
    if bidding > best:
        best = bidding
        saved_name = name

print(saved_name)