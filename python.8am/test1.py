import sys

sys.path.append("c:\\python.8am")   

import demo

b = 2000

def fun2():
    print("in fun2 of test")
    
if __name__ == "__main__":
    print(b)
    fun2()
    print(demo.a)
    demo.fun1()  
