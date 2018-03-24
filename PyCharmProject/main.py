from settings import *
from tkinter import *
from stateMachine import *
from render import *



def main():

    ######## Simulating only two ants
    # while True:
    #     A = randomAngles()
    #     A[2] = A[1]
    #     X = nextStates(A)
    #     fx = np.random.random() * (width - 20)
    #     fy = np.random.random() * (height - 20)
    #     food = [fx, fy]
    #     size = 200
    #     obs = obstacles(width, height, food, 5, 5, size)
        #
        # rendera(index, width, height, tk, canvas, X, food, obs, size)
        # A[0] = crossOver(A[0],A[1])
        # A[1] = A[0]
        # A[2] = A[0]
        # X = nextStates(A)
        # rendera(index, width, height, tk, canvas, X, food, obs, size)
    # return

    ######## Simulating all the ants
    A = randomAngles()
    X = nextStates(A)
    fx = np.random.random() * (width - 20)
    fy = np.random.random() * (height - 20)
    food = [fx, fy]
    size = 200
    obs = obstacles(width, height, food, 5, 5, size)
    fitnessAll(food,X)

    i = 1
    while True:
        print(i)
        #draw
        if i%5 == 0:
            rendera(index, width, height, tk, canvas, X, food, obs, size)
        #calc fit
        F = fitnessAll(food,X)
        db('F ', F)
        #new gen
        A = newGen(A,F)
        X = nextStates(A)
        if i == 100: break
        i = i + 1


if __name__ == "__main__":
    main()