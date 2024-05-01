i=int(input("enter a number"))
x=range(2,i)
for p in x:
    if i%p==0:
     print(i,"is not a prime number")
    else:
        print(i,"is a prime number")
