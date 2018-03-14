import numpy as np
import matplotlib.pyplot as plt

def nextState(x,a):
    return [x[0] - stepSize*np.math.sin(a), x[1] + stepSize*np.math.cos(a)]

def column(matrix, i):
    return [row[i] for row in matrix]


#### INIT
# number of steps
n = 300
#environment
xlim = 100
ylim = 100
#initial position and angle
x0 = [0,0]
a0 = 0
#length of each step
stepSize = 1
#maximum angle change per step
maxAngChangePerStep = 3.14/10


#### STATES
#angle vector
a = [a0]
np.random.seed(42)
for i in range(n):
    a.append(a[-1] + maxAngChangePerStep*np.random.normal())

#positions
x = [x0]
for i in range(n):
    x.append(nextState(x[i],a[i]))


#### PLOTS
#plot angle vector
# plt.plot(a,'.')
# plt.ylabel('some numbers')
# plt.show()

#plot route
plt.scatter(column(x,0),column(x,1))
plt.ylabel('some numbers')
# plt.xlim(-xlim,xlim)
# plt.ylim(-ylim,ylim)
plt.show()


"""
=====
Decay
=====

This example showcases a sinusoidal decay animation.
"""


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def data_gen(t=0):
    cnt = 0
    while cnt < 1000:
        cnt += 1
        t += 0.1
        yield t, np.sin(2*np.pi*t) * np.exp(-t/10.)


def init():
    ax.set_ylim(-1.1, 1.1)
    ax.set_xlim(0, 10)
    del xdata[:]
    del ydata[:]
    line.set_data(xdata, ydata)
    return line,

fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.grid()
xdata, ydata = [], []


def run(data):
    # update the data
    t, y = data
    xdata.append(t)
    ydata.append(y)
    xmin, xmax = ax.get_xlim()

    if t >= xmax:
        ax.set_xlim(xmin, 2*xmax)
        ax.figure.canvas.draw()
    line.set_data(xdata, ydata)

    return line,

ani = animation.FuncAnimation(fig, run, data_gen, blit=False, interval=10,
                              repeat=False, init_func=init)
plt.show()

