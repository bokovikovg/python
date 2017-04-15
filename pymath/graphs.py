from math import *
import matplotlib.pyplot as plt
import time

def mplot(x, y1, y2):
    fig = plt.figure(figsize=(15, 5))
    ax1 = fig.add_subplot(1, 2, 1)
    ax2 = fig.add_subplot(1, 2, 2)

    ax1.plot(x, y1)
    ax1.set_title('Quadratic')
    ax1.set_xlabel('x axis')
    ax1.set_ylabel('y label')

    ax2.plot(x, y2)
    ax2.set_title('Cubic')
    ax2.set_xlabel('x axis')
    ax2.set_ylabel('y axis')

    return fig

x = [i for i in range(101)]
y1 = [i**2 for i in x]
y2 = [i**3 for i in x]

print(mplot(x, y1, y2))
time.sleep(5)
