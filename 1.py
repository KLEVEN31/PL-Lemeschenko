import math
x=float(0.1722)
y=float(6.33)
z=float(0.000325)
s=(5*(math.atan(x))-(1/4*(math.acos(x)))*(x+3*(abs(x-y))+x**2)/((abs(x-y))*z+x**2))
print(s)
