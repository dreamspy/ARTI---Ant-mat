from settings import *
from tkinter import *
from stateMachine import *
from render import *



def main():
    ######## Simulating only two ants
    # while True:
        # A = randomAngles()
        # A[2] = A[0]
        # A[1] = A[0]
        # X = pathsFromAngles(A)
        # fx = 0
        # fy = 0
        # fx = np.random.random() * (width - 20)
        # fy = np.random.random() * (height - 20)
        # foodLocation = [fx, fy]
        # foodSize = 200
        # obs = obstacles(width, height, foodLocation, 5, 5, foodSize)
        # F = fitnessAll(foodLocation,X)
        # print('F',F)
        # rendera(index, width, height, tk, canvas, X, foodLocation, obs, foodSize)
        # A[0] = crossOver(A[0],A[1])
        # A[1] = A[0]
        # A[2] = A[0]
        # X = pathsFromAngles(A)
        # rendera(index, width, height, tk, canvas, X, foodLocation, obs, foodSize)
    # return

    ####### Simulating all the ants
    A = randomAngles()
    X = pathsFromAngles(A)
    fx = np.random.random() * (width - 20)
    fy = np.random.random() * (height - 20)
    foodLocation = [fx, fy]
    foodSize = 200
    obs = obstacles(width, height, foodLocation, 5, 5, foodSize)
    fitnessAll(foodLocation,X)

    i = 1
    while True:
        db('i',i)
        #draw
        if i%drawEveryNFrames == 1:
            rendera(index, width, height, tk, canvas, X, foodLocation, obs, foodSize)

        #calc fit
        F = fitnessAll(foodLocation,X)
        # db('F ', F)
        db("average fitness: ", np.mean(np.array(F)))
        #new gen
        A = newGen(A,F)
        X = pathsFromAngles(A)
        if i == 1000: break
        i = i + 1
        if i%moveFoodEveryNFrames == 0:
            fx = np.random.random() * (width - 20)
            fy = np.random.random() * (height - 20)
            foodLocation = [fx, fy]


if __name__ == "__main__":
    main()