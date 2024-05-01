print("begin")
data = input("enter a string: ")
i = len(data) - 1
rev_data = " "
while i >= 0:
    rev_data = rev_data + data[i]
    i = i - 1
    print(rev_data)
print("end")
