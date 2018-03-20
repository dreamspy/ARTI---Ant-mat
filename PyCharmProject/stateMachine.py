from datetime import datetime
import numpy as np

def nextStep(x, a):
    return [x[0] - stepSize*np.math.sin(a), x[1] + stepSize*np.math.cos(a)]

def getPath(a):
    x = [x0]
    for i in range(n):
        x.append(nextStep(x[i], a[i]))
    return x

def column(matrix, i):
    return [row[i] for row in matrix]

def crossOver(a1,a2):
    a = [0]
    a.append([((a1[i+1]-a1[i]) + (a2[i+1]-a2[i]))/2 for i in range(n-1)])
    return a

def randomAngles():
    A = []
    for j in range(N):
        a = [a0]
        for i in range(n):
            a.append(a[-1] + maxAngChangePerStep*np.random.normal())
        A.append(a)
    return A

def nextStates(A):
    X = []
    for i in range(N):
        X.append(getPath(A[i]))
    return X

def runTest():
    A = randomAngles()
    X = nextStates(A)

    #crossover test
    a1 = A[0]
    a2 = A[1]
    a = crossOver(a1,a2)

    #generate next gen
    # F = fitness(A)
    # select random 100 pairs
    # generate children

    #### PLOTS
    #plot angle vector
    # plt.plot(a,'.')
    # plt.ylabel('some numbers')
    # plt.show()

    #plot route
    # colors = np.random.rand(n)
    plt.scatter(column(X[0],0),column(X[0],1), marker='.')
    plt.scatter(column(X[1],0),column(X[1],1), marker='.')
    # plt.scatter(column(x,0),column(x,1), marker='*')
    # plt.scatter(column(X[3],0),column(X[3],1), marker='o')
    plt.ylabel('some numbers')
    plt.xlim(-xLength/2, xLength/2)
    plt.ylim(-yLength/2, yLength/2)
    plt.show()


if __name__ == "__main__":
    #### INIT
    # number of steps
    n = 100
    # number of ants
    N = 100
    #environment
    xLength = 100
    yLength = 100
    #initial position and angle
    x0 = [0,0]
    a0 = 0
    #length of each step
    stepSize = 1
    #maximum angle change per step
    maxAngChangePerStep = 3.14/10
    runTest()
