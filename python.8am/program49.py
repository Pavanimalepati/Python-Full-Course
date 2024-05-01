print("begin")
data = input("Enter a string: ")
c = input("Enter the search character: ")
i = 0

while i < len(data):
    if data[i] == c:
        print("Character is found")
        break
    i += 1
else:
    print("Character is not found")

print("end")
