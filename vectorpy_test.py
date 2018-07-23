from vectorpy import vector

a = vector(1.1, 3, 5)
b = vector(1, 3, 5)

print(a.cross(b))

a = vector(1.1, 3, 5)
b = vector(1, 3, 5)

print(a+b)

a = vector(1.1, 3, 5)
b = vector(1, 3, 5)

print(a-b)

a = vector(1.1, 3, 5)
b = vector(orig=a)

print(a, b)
