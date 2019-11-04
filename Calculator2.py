def AND (a, b):
    if a == 1 and b == 1: 
        return 1
    else: 
        return 0
def XOR (a, b):
    if a != b: 
        return 1
    else: 
        return 0
def OR(a, b): 
    if a == 1: 
        return 1
    elif b == 1: 
        return 1
    else: 
        return 0
def XOR1 (a, b):
    if a != b: 
        return 1
    else: 
        return 0
def AND1 (a, b):
    if a == 1 and b == 1: 
        return 1
    else: 
        return 0
x = XOR(1, 1)
y = AND(1, 1)
z = AND1(x, 0)
c = OR(y, z)
d = XOR1(x, 0)
print(d)
print(c)
10