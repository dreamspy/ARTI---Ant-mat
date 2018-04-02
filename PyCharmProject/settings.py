from tkinter import *
from math import floor

debug = True
# debug = False

#### INIT
### Drawing settings
drawEveryNRuns = 3
drawEveryNFrames = 10
tk = Tk()
width = 800
height = 600
canvas = Canvas(tk, width=width, height=height)
canvas.pack()
index = 0

### Simulation settings

# number of steps
# n = floor(2/3 * (height + width)/2 )
n = 1000
# number of ants
N = 100
# initial position and angle
x0 = [width / 2, height / 2]
# length of each step
stepSize = 1
# maximum angle change per step
maxAngChangePerStep = 3.14 / 10
# random factor for child paths
randomFactor = 0.01
moveFoodEveryNFrames = 20

### Crossower settings

# crossower methood
# 0 = average over delta angular acceleration
# 1 = splice parents at random location
# 2 = randomly weighted average
# 3 = average over angular acceleration
crossOverMethod = 1

# random method
# -1= no random added
# 0 = add random path to whole path
# 1 = add random small turn at random location for all ants
#     + add random drastic turn at random location for ants with probablility p
randomMethod = 1

# random method 0 settings
# control amount of random path added in method 0
randomCrossOwerFactor = 0.5

# random method 1 settings
normalVariance = 0.1
