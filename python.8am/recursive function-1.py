i = 1

def myfunc():
    global i
    print("welcome", i)
    i = i + 1

while i <= 4:
    myfunc()

myfunc()
