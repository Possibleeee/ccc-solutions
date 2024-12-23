a = int(input())
c = 0

for _ in range(a):
    b = input()
    c += 1500 if b == "Poblano" else 6000 if b == "Mirasol" else 15500 if b == "Serrano" else 40000 if b == "Cayenne" else 75000 if b == "Thai" else 125000

print(c)