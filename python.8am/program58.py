x=range(1,101)
es=0
os=0
for p in x:
    if p%2==0:
     es=es+p
    else:
        os=os+p
        print("sum of even numbers",es)
        print("sum of odd numbers",os)
