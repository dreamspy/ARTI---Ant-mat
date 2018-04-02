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

    chrashed = [obj]* len(X)
    ate = [obj]* len(X)

    fx = np.random.random() * (width - 20)
    fy = np.random.random() * (height - 20)
    foodLocation = [fx, fy]
    foodSize = 200
    obs = obstacles(width, height, foodLocation, 1, 1, foodSize)
    fitnessAll(foodLocation,X)
    eaten = 0


    i = 0
    while True:
        db("\ni",i)
        collisionObstacles(X, obs, chrashed, foodSize)
        eaten = collisionFood(X, ate, foodLocation, eaten)

        #draw
        if i%drawEveryNRuns == 0:
            rendera(index, width, height, tk, canvas, X, foodLocation, obs, foodSize, chrashed, ate, eaten)

        #calc fit
        F = fitnessAll(foodLocation,X)

        #new gen
        angularAcceleration = newAngGen(angularAcceleration,F)
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