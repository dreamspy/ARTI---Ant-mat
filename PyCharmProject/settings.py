from tkinter import *

debug = True
debug = False

#### INIT
# number of steps
n = 300
# number of ants
N = 50
# environment
xLength = 100
yLength = 100
# initial position and angle
x0 = [0, 0]
# length of each step
stepSize = 1
# maximum angle change per step
maxAngChangePerStep = 3.14 / 10

# Drawing settings
tk = Tk()
canvas = Canvas(tk, width=800, height=600)
canvas.pack()
width = 800
height = 600
index = 0