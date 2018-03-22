from settings import *
from tkinter import *
from stateMachine import *
from render import *
# import stateMachine

def main():
    A = randomAngles()
    X = nextStates(A)
    fx = np.random.random() * (width - 20)
    fy = np.random.random() * (height - 20)
    food = [fx, fy]
    size = 200
    obs = obstacles(width, height, food, 5, 5, size)

    while True:
        rendera(index, width, height, tk, canvas, X, food, obs, size)
        runTest()

if __name__ == "__main__":
    main()