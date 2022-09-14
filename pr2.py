import math
x=16.55*10**-3
y=-2.75
z=0.15
s=(((10*((x**0.33)+(x**(y+2)))))**0.5)*(((math.asin(z)**2))-(math.fabs(x-y)))
print(s)