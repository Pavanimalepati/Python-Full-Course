def outer():
    def inner():
        print("in inner")
    inner() 
    print("in outer")
    return inner  

myvar = outer() 
