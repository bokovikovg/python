import sys
import math
import cmath
import numpy as np
import array as ar
#function and its derivative

def g(z, alpha):
    return (z*z*z*z*z + alpha*z + 1)

def dgdx(z, alpha):
    return (5*z*z*z*z + alpha)

#script itself

root1 = [1.005 + 0.937j, 1.005 - 0.937j, -0.331 + 0.0j, -0.839 - 0.943j, -0.839 + 0.943j]
eps = 0.01
alpha = 3.00000 + 0.00000j
roots = list(); alphas = list();
alphas.append(alpha)
arr = list(list()) 
#arr.append(root1)
for k in range(0, 5):
    t = 0.1; i = 0;
    roots.clear()
    roots.append(root1[k])
    while t <= 2*math.pi:
        alpha = 3*cmath.exp((0.0+1.0j)*t)
        z1 = roots[i]
        while True:
            n_z1 = z1 - g(z1, alpha)/dgdx(z1, alpha) 
            if abs(z1 - n_z1) < eps:
                z1 = n_z1
                break
            z1 = n_z1
        roots.append(z1); alphas.append(alpha);
        t += 2*math.pi/70 
        i += 1
    arr.append(roots)

for i in range(0, 5):
    print('{} circle, {} \n'.format(i, arr[i]))
