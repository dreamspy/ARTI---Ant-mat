from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt

def nextState(x,a):
    return [x[0] - stepSize*np.math.sin(a), x[1] + stepSize*np.math.cos(a)]

def column(matrix, i):
    return [row[i] for row in matrix]


#### INIT
# number of steps
n = 10
# number of ants
N = 5
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
A = []
# np.random.seed()
for j in range(N):
    a = [a0]
    for i in range(n):
        a.append(a[-1] + maxAngChangePerStep*np.random.normal())
    A.append(a)

#positions
X = []
x = [x0]
for j in range(N):
    for i in range(n):
        x.append(nextState(X[j][i],A[j][i]))
    X.append(x)

# print(X[0])
# print("XXXXXXXXXXXXXXXXXXXXXX")
# print(X[1])
#### PLOTS
#plot angle vector
# plt.plot(a,'.')
# plt.ylabel('some numbers')
# plt.show()

#plot route
# colors = np.random.rand(n)
plt.scatter(column(X[0],0),column(X[0],1), marker='.')
plt.scatter(column(X[1],0),column(X[1],1), marker='+')
plt.ylabel('some numbers')
# plt.xlim(-xlim,xlim)
# plt.ylim(-ylim,ylim)
plt.show()



