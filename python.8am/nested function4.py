def outer():
    msg = "pavani"
    
    def inner():
        nonlocal msg
        msg = "python"
        print(msg)
    
    inner() 
    print(msg)  

outer()

