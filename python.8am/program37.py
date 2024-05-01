print("begin")
es = 0
os = 0
i = 1
while i <= 100:
    if i % 2 == 0:
        es = es + i
    else:
        os = os + i
    i = i + 1
    print("even number sum is", es)
    print("odd numbers sum is", os)
print("end")
