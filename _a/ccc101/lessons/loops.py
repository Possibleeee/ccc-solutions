"""
1 1
1 2
1 3
2 1
2 2
2 3
3 1
3 2
3 3
"""

# nested loop
for i in range(1, 4):
    for o in range(1,4):
        print(i, o)

print("#####################")

s = "abc"
for i in s:
    for o in s:
        print(i, o)