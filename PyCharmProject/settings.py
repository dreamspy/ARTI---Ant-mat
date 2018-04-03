from tkinter import *
from math import floor

# debug = True
debug = False

#### INIT
### Drawing settings
drawEveryNRuns = 5
drawEveryNFrames = 20
tk = Tk()
width = 800
height = 600
canvas = Canvas(tk, width=width, height=height)
canvas.pack()
index = 0

### Simulation settings
# nr of generated obstacles
nrOfHorizObstacles = 2
nrOfVertObstacles = 2

# n: number of steps
n = 1500
# N: number of ants
N = 100
# x0: initial position and angle
x0 = [width / 2, height / 2]
# stepSize: length of each step
stepSize = 1
# maximum angle change per step
maxAngChangePerStep = 3.14 / 10
# step limit for every simulation of an environment
stepLimit = 300
# step limit for every simulation of food location until resetting population to random
maxNrOfStepsPerFood = 50

### Food Settings
#number of foods per environment
numberOfFoods = 5
#number of environments per simulation
numberOfEnvs = 10
#obstacle size
obsSize = 200
#nr of ants that  need to reach food until depleted
bitesPerFood = 100

