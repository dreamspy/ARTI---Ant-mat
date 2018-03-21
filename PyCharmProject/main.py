from settings import *
from tkinter import *
from stateMachine import *
from render import *
# import stateMachine

def main():
    tk = Tk()
    canvas = Canvas(tk, width=800, height=600)
    canvas.pack()
    width = 800
    height = 600
    index = 0
    A = randomAngles()
    X = nextStates(A)

    while True:
        rendera(index, width, height, tk, canvas, X)
        runTest()

if __name__ == "__main__":
    main()