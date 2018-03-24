from settings import *
import numpy as np

def db(y,x):
    if debug:
        print(y)
        if type(x) is list:
            print(np.array(x))
        else:
            print(x)