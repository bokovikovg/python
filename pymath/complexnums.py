import sys
import math
import cmath 

y = math.sqrt(3); x = 1;
w0 = complex(x, y)

z = complex(4.4, 3.5)
w = complex(3.2, -5.3)
z1 = z + w
print('z + w = {} + {}*i'.format(z1.real, z1.imag))
print('z * w = {} + {}*i'.format(z1.real, z1.imag))
sinz = cmath.sin(z) 
print('w0 = {} + {}i, arg(w0) = {}'.format(x, y, cmath.phase(w0)))

print('sinz  = {} + {}*i'.format(sinz.real, sinz.imag))
ls = cmath.polar(w0) 
print(ls)
print(cmath.exp((0.000+1.0000j)*cmath.pi))
