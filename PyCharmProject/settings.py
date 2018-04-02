from tkinter import *
from math import floor

debug = True
# debug = False

#### INIT
### Drawing settings
drawEveryNRuns = 5
drawEveryNFrames = 5
tk = Tk()
width = 800
height = 600
canvas = Canvas(tk, width=width, height=height)
canvas.pack()
index = 0

### Simulation settings
# number of steps
# n = floor(2/3 * (height + width)/2 )
n = 500
# number of ants
N = 100
# N = 3
# initial position and angle
x0 = [width/2,height/2]
# length of each step
stepSize = 1
# maximum angle change per step
maxAngChangePerStep = 3.14/10
#random factor for child paths
randomFactor = 0.01
moveFoodEveryNFrames = 20