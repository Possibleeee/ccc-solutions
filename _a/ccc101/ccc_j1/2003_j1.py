ouchie_L = int(input())
spaces = int(input())
handle_L = int(input())

for _ in range(ouchie_L):
    print(("*" + " " * spaces) * 2, end= "")
    print("*")

print(("*" + "*" * spaces) * 2 + "*")

for _ in range(handle_L):
    print(" " * (spaces + 1) + "*")