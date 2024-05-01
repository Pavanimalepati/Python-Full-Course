data=input("enter a string")
s=input("enter a search character")
for p in data:
    if p==s:
        print("character is found")
        break
    else:
        print("character is not found")
