from tkinter import *
from math import floor

debug = True
# debug = False

#### INIT
### Drawing settings
drawEveryNRuns = 1
drawEveryNFrames = 30
tk = Tk()
width = 800
height = 600
canvas = Canvas(tk, width=width, height=height)
canvas.pack()
index = 0

### Simulation settings

# number of steps
# n = floor(2/3 * (height + width)/2)
n = 1500
# number of ants
N = 100
# initial position and angle
x0 = [width / 2, height / 2]
# length of each step
stepSize = 1
# maximum angle change per step
maxAngChangePerStep = 3.14 / 10
# step limit for every run of a environment
stepLimit = 200

### Food Settings
numberOfFoods = 5
numberOfEnvs = 10
obsSize = 200
bitesPerFood = 100

