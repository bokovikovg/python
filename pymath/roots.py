import sys
import math
import cmath
import numpy as np
import array as ar
import time
from sympy import *
import matplotlib.pyplot as plt

init_printing(use_unicode=True)
#function and its derivative

def g(z, alpha):
    return (z*z*z*z*z + alpha*z + 1)

def dgdz(z, alpha):
    return (5*z*z*z*z + alpha)

#plot function

def visuals(arr, alphas, num):
    #fig1 = plt.figure(figsize=(15, 5))
    #fig2 = plt.figure(figsize=(15, 5))
    x1 = x2 = x3 = x4 = x5 = []
    y1 = y2 = y3 = y4 = y5 = []
    for i in range(0, num):
        x1.append(arr[0][i].real); y1.append(arr[0][i].imag)
        x2.append(arr[1][i].real); y2.append(arr[1][i].imag)
        x3.append(arr[2][i].real); y3.append(arr[2][i].imag)
        x4.append(arr[3][i].real); y4.append(arr[3][i].imag)
        x5.append(arr[4][i].real); y5.append(arr[4][i].imag)
    print(x1)
    plt.axis([-10, 10, -10, 10])
    plt.plot(x1, y1)
    #plt.plot(x2, y2)
    #plt.plot(x3, y3)
    #plt.plot(x4, y4)
    #plt.plot(x5, y5)
    plt.show()




#script itself
deg = 5
delta = 360
roots = list(); alphas = list();
arr = [[0 for j in range(delta)] for i in range(deg)]
step = 2*math.pi/delta
start_roots = [1.005 + 0.937j, 1.005 - 0.937j, -0.331 + 0.0j, -0.839 - 0.943j, -0.839 + 0.943j]
theta = np.arange(0.0, 2*math.pi, 0.01)
for k in range(deg):
    eps = 0.001
    alpha = 3.00000 + 0.00000j
    t = 0.1
    i = 0
    roots.clear()
    roots.append(start_roots[k])
    alphas.clear()
    alphas.append(alpha)
    while t < 2*math.pi:
        alpha = (3 - math.sin(0))*cmath.exp((0.0+1.0j)*t)
        z1 = roots[i]
        while True:
            n_z1 = z1 - g(z1, alpha)/dgdz(z1, alpha)
            if abs(z1 - n_z1) < eps:
                z1 = n_z1
                break
            z1 = n_z1
        roots.append(z1)
        alphas.append(alpha)
        t += step
        i += 1
    #print('the cycle for {0.real:.3f}{0.imag:+.3f}j\n'.format(start_roots[k]))
    #for j in range(0, roots.__len__()):
    #    print('{0.real:.3f}{0.imag:+.3f}j'.format(roots[j]))
    for u in range(0, roots.__len__()):
        arr[k][u] = roots[u]
    #print(roots)
print('{}'.format(alphas.__len__()))
#print(arr[0][6], arr[1][6], arr[2][6], arr[3][6], arr[4][6], arr[4][6], end='\n')
#print["alpha={}\nroots={}\n".format(alphas[356-1], arr[:][356-1])]
s1 = []
t1 = []
s2 = []
t2 = []
s3 = []
t3 = []
s4 = []
t4 = []
s5 = []
t5 = []
print('\nlen={}\n'.format(arr[0].__len__()))
slice = delta - 5
for m in range(delta):
    s1.append(arr[0][m].real)
    t1.append(arr[0][m].imag)
    s2.append(arr[1][m].real)
    t2.append(arr[1][m].imag)
    s3.append(arr[2][m].real)
    t3.append(arr[2][m].imag)
    s4.append(arr[3][m].real)
    t4.append(arr[3][m].imag)
    s5.append(arr[4][m].real)
    t5.append(arr[4][m].imag)
print('{}\nand\n{}'.format(s1, t1))
plt.axis([-2, 2, -2, 2])
plt.plot(s1[:slice], t1[:slice])
plt.plot(s2[:slice], t2[:slice])
plt.plot(s3[:slice], t3[:slice])
plt.plot(s4[:slice], t4[:slice])
plt.plot(s5[:slice], t5[:slice])
plt.show()
#visuals(arr, alphas, delta)