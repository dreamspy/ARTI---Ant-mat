from settings import *
from tkinter import *
from stateMachine import *
from environment import *
from render import *


def main():
    angularAcceleration = randomAngularAcceleration()
    A = anglesFromAcceleration(angularAcceleration)
    X = pathsFromAngles(A)
    obj = [False, 0]

    chrashed = [obj] * len(X)
    ate = [obj] * len(X)

    numberOfFoods = 5

    foodLocations = [newFood(width, height,0) for i in range(numberOfFoods)]
    foodSize = 200
    obs = obstacles(width, height, foodLocations, 1, 1, foodSize, 0)
    fitnessAll(foodLocations[0], X, ate, chrashed)
    eaten = 0
    foodLocation = foodLocations[0]



################################3
    testEnvs = [[i,[i+j for j in range(5)]] for i in range(10)]
    counter = 0
    for env in testEnvs:
        obsSeed = env[0]
        foodSeeds = env[1]
        foodLocations = [newFood(width,height, seed) for seed in foodSeeds]
        obs = obstacles(width, height, foodLocations, 2, 3, foodSize, obsSeed)
        chrashed = [obj] * len(X)
        ate = [obj] * len(X)

        db("counter", counter)
        db("eaten", eaten)

        nrOfSteps = 0

        for foodLocation in foodLocations:
            eaten = 0
            chrashed = [obj] * len(X)
            ate = [obj] * len(X)
            collisionObstacles(X, obs, chrashed, foodSize)
            eaten = collisionFood(X, ate, foodLocation, eaten)
            while eaten <= 100:
                collisionObstacles(X, obs, chrashed, foodSize)
                eaten = collisionFood(X, ate, foodLocation, eaten)
                if nrOfSteps%drawEveryNRuns == 0:
                    rendera(index, width, height, tk, canvas, X, foodLocation, obs, foodSize, chrashed, ate, eaten)

                # calc fit
                F = fitnessAll(foodLocation, X, ate, chrashed)

                # new gen
                angularAcceleration = newAngGen(angularAcceleration, F)
                A = anglesFromAcceleration(angularAcceleration)
                X = pathsFromAngles(A)

                chrashed = [obj] * len(X)
                ate = [obj] * len(X)
                nrOfSteps += 1
                db("eaten", eaten)

        counter += 1

    return
    i = 0
    while True:
        db("\ni", i)
        collisionObstacles(X, obs, chrashed, foodSize)
        eaten = collisionFood(X, ate, foodLocation, eaten)

        # draw
        if i % drawEveryNRuns == 0:
            rendera(index, width, height, tk, canvas, X, foodLocation, obs, foodSize, chrashed, ate, eaten)

        # calc fit
        F = fitnessAll(foodLocation, X, ate, chrashed)

        # new gen
        angularAcceleration = newAngGen(angularAcceleration, F)
        A = anglesFromAcceleration(angularAcceleration)
        X = pathsFromAngles(A)

        chrashed = [obj] * len(X)
        ate = [obj] * len(X)

        i = i + 1

        if eaten >= 100:
            fx = np.random.random() * (width - 20)
            fy = np.random.random() * (height - 20)
            foodLocation = [fx, fy]
            eaten = 0
        # db("eaten", eaten)


def pShape(X):
    print(np.array(X).shape)


if __name__ == "__main__":
    main()







