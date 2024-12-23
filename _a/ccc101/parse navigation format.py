dict = {
    "L" : "LEFT",
    "R" : "RIGHT",
}

while True:
    a = input()
    b = input()
    print(f"Turn {dict[a]} " + ("onto " + b + " street" if b != "SCHOOL" else f"into your {dict[b]}") + ".")
    if b == "SCHOOL":
        break