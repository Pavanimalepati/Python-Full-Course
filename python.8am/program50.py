print("begin")
x = int(input("enter a number"))
i = 2

while i < x:
    if x % i == 0:
        print(x, "is not a prime number")
        break
    i = i + 1
else:
    print(x, "is a prime number")

print("end")
