print("begin")
data= input("enter a string: ")
i = len(data)-1
rev_data=""
while i>0:
    rev_data=rev_data+data[i]
    i=i-1
    print(rev_data)

if data==rev_data:
    print(data,"is not a palindrome")
else:
    print(data,"is a palindrome")
    print("end")
