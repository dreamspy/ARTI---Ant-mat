from tkinter import *
import random
import time
from datetime import datetime
import numpy as np

def rendera(index, width, height, tk, canvas, X, food, obs, size):
    while index < len(X[1]):
        canvas.delete("all")
        #canvas.create_oval((width/2) - (width/30), (height/2) - (height/30), (width/2) + (width/30), (height/2) + (height/30), fill="brown")
        canvas.create_oval(food[0], food[1], food[0] + 20, food[1] + 20, fill="brown")
        a = 0
        while a < len(obs):
            for i in obs[0]:
                canvas.create_rectangle(i[0], i[1], i[0] + size, i[1] + 5, fill="black")
            for i in obs[1]:
                canvas.create_rectangle(i[0], i[1], i[0] + 5, i[1] + size, fill="black")
            a += 1
        canvas.create_text(50, 50, font="13", text=index)
        for i in X:
            if index < len(i):
                x0 = i[index][0] + (width / 2)
                y0 = i[index][1] + (height / 2)
                x1 = x0+5
                y1 = y0+5
            canvas.create_rectangle(x0, y0, x1, y1, fill="red")
        #tk.update_idletasks()
        tk.update()
        time.sleep(0.001)
        index += 1

def obstacles(width, height, food, amountLong, amountTall, size):
    obs = []
    obsLong = []
    obsTall = []
    i = 0
    while i < amountLong:
        x = np.random.random() * (width - size)
        y = np.random.random() * (height - size)
        while (x > food[0] and x < (food[0] + size)) and (y > food[1] and y < (food[1] + size)):
            x = np.random.random() * (width - size)
            y = np.random.random() * (height - size)
        obj = [x, y]
        obsLong.append(obj)
        i += 1
    i = 0
    while i < amountTall:
        x = np.random.random() * (width - size)
        y = np.random.random() * (height - size)
        while (x > food[0] and x < (food[0] + size)) and (y > food[1] and y < (food[1] + size)):
            x = np.random.random() * (width - size)
            y = np.random.random() * (height - size)
        obj = [x, y]
        obsTall.append(obj)
        i += 1
    if obsLong:
        obs.append(obsLong)
    if obsTall:
        obs.append(obsTall)
    return obs
#DRAWINGS
