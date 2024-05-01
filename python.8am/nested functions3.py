def outer():
    msg = "pavani"
    
    def inner():
        msg = "python"
        print(msg)
    
    inner() 
    print(msg)  

outer()

