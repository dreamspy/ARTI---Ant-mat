from datetime import datetime
from scipy.spatial import distance
from settings import *
import numpy as np
from debug import *
from math import exp
from math import floor
from math import ceil


def nextStep(x, a):
    return [x[0] - stepSize * np.math.sin(a), x[1] + stepSize * np.math.cos(a)]


def getPath(a):
    x = [x0]
    for i in range(n):
        x.append(nextStep(x[i], a[i]))
    return x


# return column i from matrix
def column(matrix, i):
    return [row[i] for row in matrix]


def pShape(X):
    print(np.array(X).shape)


# create child from parents
def crossOver(angAcc1, angAcc2):
    if crossOverMethod == 0:
        # generate child using average angular acceleration change
        top = [(angAcc1[0] + angAcc2[0]) / 2]
        bottom = [((angAcc1[i + 1] + angAcc1[i]) + (angAcc2[i + 1] - angAcc2[i])) / 2 for i in range(n - 1)]
        c = np.concatenate((top, bottom))

    elif crossOverMethod == 1:
        # generate child using random splice
        spliceLocation = int(np.random.uniform(0, n, 1))
        top = angAcc1[:spliceLocation]
        bottom = angAcc2[spliceLocation:]
        c = np.concatenate((top, bottom))

    elif crossOverMethod == 2:
        # generate child using random weight
        w1 = np.random.uniform(0, 1, 1)[0]
        w2 = 1 - w1
        c = [w1 * angAcc1[i] + w2 * angAcc2[i] for i in range(n)]

    elif crossOverMethod == 3:
        # generate child using average angular acceleration
        c = [(angAcc1[i] + angAcc2[i]) / 2 for i in range(n)]

    else:
        # fallback
        c = angAcc1

    if randomMethod == 0:
        # add random path
        randomVector = randomCrossOwerFactor * maxAngChangePerStep * (np.random.uniform(-1, 1, n))
        c = c + randomVector

    elif randomMethod == 1:
        # add random turn at random place
        turnLocation = int(np.random.uniform(0, n, 1))
        randomAcceleration = np.random.normal(0, normalVariance, 1)[0]
        c[turnLocation] += randomAcceleration

        # randomVector = randomFactor*maxAngChangePerStep*(np.random.uniform(-1,1,n))

        return c


# returns (1,N) dimensional random angle vector
def randomAngleVector():
    a = [3.14 * np.random.uniform(-1, 1, 1)]
    for i in range(n - 1):
        a.append(a[-1] + maxAngChangePerStep * (np.random.uniform(-1, 1, 1)))
    return a


# returns (n,N) dimensional random angle array
def randomAngularAcceleration():
    A = []
    for j in range(N):
        a = [0]
        for i in range(n - 1):
            a.append(maxAngChangePerStep * (np.random.uniform(-1, 1, 1)[0]))
        A.append(a)
    return A


# returns path from angles A
def pathsFromAngles(A):
    X = []
    for i in range(N):
        X.append(getPath(A[i]))
    return X


# input (n,N) dimensional angle acceleration array
# returns (n,N) dimensional angle array
def anglesFromAcceleration(angularAccelleration):
    A = []
    for j in range(N):
        a = [0]
        # a = [3.14 * np.random.uniform(-1, 1, 1)]
        for i in range(n - 1):
            a.append(a[i] + angularAccelleration[j][i + 1])
        A.append(a)
    return A


# return the closest node in "nodes", wrt "node"
def closest_node(node, nodes):
    closest_index = distance.cdist([node], nodes).argmin()
    return nodes[closest_index]


# food: location of foods
# nods: a path as a list of nodes
def fitness(food, nodes):
    closest = closest_node(food, nodes)
    dist = np.math.sqrt((food[0] - closest[0]) ** 2 + (food[1] - closest[1]) ** 2)
    score = 1 / (1 + dist)
    return score


# calculate fitness for all the dudes
def fitnessAll(food,X,ate,chrashed):
    F = []
    for i in range(N):
        path_bonus = 0
        if ate[i][0]:
            path_bonus += np.math.sqrt((width/2 - food[0])**2 + (height/2 - food[1])**2)/ate[i][1]
        if chrashed[i][0]:
            if not ate[i][0]:
                F.append(0)
                continue
            if chrashed[i][1] < ate[i][1]:
                F.append(0)
                continue
        F.append(fitness(food,X[i]) + path_bonus)
    return F


def magnitude(v):
    return np.math.sqrt(sum(v[i] * v[i] for i in range(len(v))))


# normalize vector to have sum = 1
def normalize(v):
    vSum = sum(v)
    return [v[i] / vSum for i in range(len(v))]


# check if list a is in the "list of lists" b
def isIn(a, b):
    aInv = [a[1], a[0]]
    for i in range(len(b)):
        if np.array_equal(a, b[i]):
            return True
        elif np.array_equal(aInv, b[i]):
            return True
    return False


# generate new gene pool
def newGen(A, F):
    # print("\nspawning New Gen:")
    # db("old A", A)
    newA = []
    parents = []
    F = normalize(F)
    # create parent pairs
    for i in range(N):
        # select random parents
        pTemp = np.random.choice(N, 2, p=F)
        # make sure theyre note the same
        while pTemp[0] == pTemp[1]:
            pTemp = np.random.choice(N, 2, p=F)
        # make sure no pairs appear twice
        while isIn(pTemp, parents):
            pTemp = np.random.choice(N, 2, p=F)
            while pTemp[0] == pTemp[1]:
                pTemp = np.random.choice(N, 2, p=F)
        parents.append(pTemp)
    # generate new genes
    for i in range(N):
        a = (crossOver(A[parents[i][0]], A[parents[i][1]]))
        newA.append(a)
    return newA


def newAngGen(A, F):
    # print("\nspawning New Gen:")
    # db("old A", A)
    newA = []
    parents = []
    F = normalize(F)
    # create parent pairs
    for i in range(N):
        # select random parents
        pTemp = np.random.choice(N, 2, p=F)
        # make sure theyre note the same
        while pTemp[0] == pTemp[1]:
            pTemp = np.random.choice(N, 2, p=F)
        # make sure no pairs appear twice
        while isIn(pTemp, parents):
            pTemp = np.random.choice(N, 2, p=F)
            while pTemp[0] == pTemp[1]:
                pTemp = np.random.choice(N, 2, p=F)
        parents.append(pTemp)
    # generate new genes
    for i in range(N):
        a = (crossOver(A[parents[i][0]], A[parents[i][1]]))
        newA.append(a)
    return newA


def runTest():
    A = randomAngles()
    X = pathsFromAngles(A)

    # crossover test
    a1 = A[0]
    a2 = A[1]
    a = crossOver(a1, a2)

    # generate next gen
    # F = fitness(A)
    # select random 100 pairs
    # generate children

    #### PLOTS
    # plot angle vector
    # plt.plot(a,'.')
    # plt.ylabel('some numbers')
    # plt.show()

    # plot route
    # colors = np.random.rand(n)
    # plt.scatter(column(X[0],0),column(X[0],1), marker='.')
    # plt.scatter(column(X[1],0),column(X[1],1), marker='.')
    # plt.scatter(column(x,0),column(x,1), marker='*')
    # plt.scatter(column(X[3],0),column(X[3],1), marker='o')
    # plt.ylabel('some numbers')
    # plt.xlim(-xLength/2, xLength/2)
    # plt.ylim(-yLength/2, yLength/2)
    # plt.show()

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

