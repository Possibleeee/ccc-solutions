c = input()
c = input()

a = c.count("A")
b = c.count("B")

print("A" if a > b else "B" if b > a else "Tie")