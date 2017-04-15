import math
from sympy import *

init_printing(use_unicode=True)

n = int(input('enter n='))

ring = [i for i in range(0, n)]

for i in ring:
    if (i**2) % n ==i:
        print(i)

R =[[[a, b], [2*b % 7, (a+b)%7]] for a in range(0, 7) for b in range(0, 7)]
print(R)
print(len(R))
k = 0
for i in range(0, len(R)):
    for j in range(i, len(R)):
        if R[i]==R[j]:
            k += 1
k

S = [Matrix(i) for i in R]

S
