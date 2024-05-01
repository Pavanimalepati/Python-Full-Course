import pack1.A
from pack1.B import i, j, fun3, fun4
import pack1.spack1.C as c
from pack1.spack1.D import *
print(pack1.A.a)
print(pack1.A.b)
pack1.A.fun1()
pack1.A.fun2()  # Corrected pack.A to pack1.A
print(i)
print(j)
fun3()
fun4()
print(c.p)
print(c.q)
c.fun5()
c.fun6()
print(x)
print(y)
fun7()  # Assuming fun7 and fun8 are from pack1.spack1.D
fun8()  # Assuming fun7 and fun8 are from pack1.spack1.D
