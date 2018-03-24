from datetime import datetime
from scipy.spatial import distance
from settings import *
import numpy as np
from debug import *

def nextStep(x, a):
    return [x[0] - stepSize*np.math.sin(a), x[1] + stepSize*np.math.cos(a)]

def getPath(a):
    x = [x0]
    for i in range(n):
        x.append(nextStep(x[i], a[i]))
    return x

def column(matrix, i):
    return [row[i] for row in matrix]

def crossOver(A1, A2):
    # print("running crossover")
    db("running crossover", [])
    db("A1[0]",A1[0])
    db("A2[0]",A2[0])

    a = [(A1[0] + A2[0]) / 2]
    db('a',a)
    b = [((A1[i + 1] + A1[i]) + (A2[i + 1] - A2[i])) / 2  for i in range(n - 1)]
    c = np.vstack((a,b))
    # c=a
    return c

def randomAngles():
    A = []
    for j in range(N):
        a =  [3.14*np.random.uniform(-1,1,1)]
        for i in range(n):
            a.append(a[-1] + maxAngChangePerStep*(np.random.uniform(-1,1,1)))
        A.append(a)
    return A

def nextStates(A):
    X = []
    for i in range(N):
        X.append(getPath(A[i]))
    return X

def closest_node(node, nodes):
    closest_index = distance.cdist([node], nodes).argmin()
    return nodes[closest_index]

def fitness(food, nodes):
    closest = closest_node(food, nodes)
    dist = np.math.sqrt((food[0] - closest[0]) ** 2 + (food[1] - closest[1]) ** 2)
    score = 1/(1+dist)
    return score

def fitnessAll(food,X):
    F = []
    fitness
    for i in range(N):
        F.append(fitness(food,X[i]))
    return F

def magnitude(v):
    return np.math.sqrt(sum(v[i] * v[i] for i in range(len(v))))

def normalize(v):
    vSum = sum(v)
    return [ v[i]/vSum  for i in range(len(v)) ]

def isin(a,b):
    aInv = [a[1],a[0]]
    for i in range(len(b)):
        if np.array_equal(a,b[i]):
            return True
        elif np.array_equal(aInv,b[i]):
            return True
    return False

def newGen(A,F):
    print("\nspawning New Gen:")
    db("old A", A)
    newA = []
    parents = []
    F = normalize(F)
    for i in range(N):
        pTemp = np.random.choice(N,2,p=F)
        while pTemp[0] == pTemp[1]:
            pTemp = np.random.choice(N,2,p=F)
        while isin(pTemp,parents):
            pTemp = np.random.choice(N,2,p=F)
            while pTemp[0] == pTemp[1]:
                pTemp = np.random.choice(N,2,p=F)
        parents.append(pTemp)
    print("parents: ",parents)
    for i in range(N):
        a = (crossOver(A[parents[i][0]],A[parents[i][1]]))
        newA.append(a)
    db("newA", newA)

    return newA


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
    #plt.scatter(column(X[0],0),column(X[0],1), marker='.')
    #plt.scatter(column(X[1],0),column(X[1],1), marker='.')
    # plt.scatter(column(x,0),column(x,1), marker='*')
    # plt.scatter(column(X[3],0),column(X[3],1), marker='o')
    #plt.ylabel('some numbers')
    #plt.xlim(-xLength/2, xLength/2)
    #plt.ylim(-yLength/2, yLength/2)
    #plt.show()


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
