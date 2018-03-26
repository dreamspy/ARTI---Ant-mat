from tkinter import *

debug = True
# debug = False

#### INIT
### Drawing settings
drawEveryNFrames = 5
tk = Tk()
canvas = Canvas(tk, width=800, height=600)
canvas.pack()
width = 800
height = 600
index = 0

### Simulation settings
# number of steps
n = 500
# number of ants
N = 50
# initial position and angle
x0 = [width/2,height/2]
# length of each step
stepSize = 1
# maximum angle change per step
maxAngChangePerStep = 3.14 / 10
#random factor for child paths
randomFactor = 0.05

moveFoodEveryNFrames = 20