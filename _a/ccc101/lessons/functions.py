# function is a group of statement
def div_mod(a, b):
    c = a // b
    d = a % b
    return c, d

result = div_mod(8, 3)
print(result)

print(div_mod(5000, 25))
# used to quickly reuse code

def aFunction():
    # woah, much empty!
    pass

r = aFunction()
print(r)