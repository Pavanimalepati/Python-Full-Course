x = bytearray()
print(x)
print(type(x))
print(len(x))
for i in x:
    print(i)

y = bytearray(5)
print(y)
print(type(y))
print(len(y))
for j in y:
    print(j)
y[2] = 99  
for m in y:
    print(m)

z = bytearray([10, 20, 30, 40])
print(z)
print(type(z))
print(len(z))
for k in z:
    print(k)

p = bytearray('pavani', "utf-8")  
print(p)
for q in p:
    print(q)
