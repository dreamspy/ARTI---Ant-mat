from tkinter import *
import random
import time
from datetime import datetime
import numpy as np


def rendera(index, width, height, tk, canvas, X):
    while index < len(X[1]):
        canvas.delete("all")
        canvas.create_oval((width/2) - (width/30), (height/2) - (height/30), (width/2) + (width/30), (height/2) + (height/30), fill="brown")
        for i in X:
            if index < len(i):
                x0 = i[index][0] + (width / 2)
                y0 = i[index][1] + (height / 2)
                x1 = x0+5
                y1 = y0+5
            canvas.create_rectangle(x0, y0, x1, y1, fill="red")

        canvas.create_text(50, 50, font="13", text=index)
        #tk.update_idletasks()
        tk.update()
        time.sleep(0.001)
        index += 1
#DRAWINGS
