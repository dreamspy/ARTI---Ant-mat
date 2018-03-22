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
    f = [fx, fy]

    while True:
        rendera(index, width, height, tk, canvas, X, f)
        runTest()

if __name__ == "__main__":
    main()