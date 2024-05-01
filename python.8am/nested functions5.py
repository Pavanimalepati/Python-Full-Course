x=1000
p=1234
q=1111
def outer():
    y=2000
    p=5678
    q=2222
    def inner():
        global q
        z=3000
        print(x)
        print(y)
        print(z)
        print(p)
        print(q)
    inner()
outer()
