from tkinter import *
import random
import time
from datetime import datetime
import numpy as np
from settings import *

def rendera(index, width, height, tk, canvas, X, food, obs, size, chrashed, ate, eaten):
    while index < len(X[1]):
        canvas.delete("all")
        collisionObstacles(X, obs, chrashed, index, size)
        eaten = collisionFood(X, ate, index, food, eaten)

        bla = 0

        for i in ate:
            if i[0] == True:
                bla+=1


        eaten = eaten+bla

        foodsize = (50-eaten/100)/2

        if foodsize <= 5:
            foodsize = 5

        #canvas.create_oval((width/2) - (width/30), (height/2) - (height/30), (width/2) + (width/30), (height/2) + (height/30), fill="brown")
        canvas.create_oval(food[0], food[1], food[0] + foodsize, food[1] + foodsize, fill="brown")
        a = 0
        while a < len(obs):
            for i in obs[0]:
                canvas.create_rectangle(i[0], i[1], i[0] + size, i[1] + 5, fill="black")
            for i in obs[1]:
                canvas.create_rectangle(i[0], i[1], i[0] + 5, i[1] + size, fill="black")
            a += 1
        canvas.create_text(50, 50, font="13", text=index)
        num = 0
        for i in X:
            if chrashed[num][0] == False:
                if ate[num][0] == False:
                    if index < len(i):
                        x0 = i[index][0]
                        y0 = i[index][1]
                        x1 = x0+5
                        y1 = y0+5
                    canvas.create_rectangle(x0, y0, x1, y1, fill="red")
            num += 1
            #tk.update_idletasks()
        tk.update()
        time.sleep(0.01)
        index += drawEveryNFrames

    return eaten

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

def collisionObstacles(X, obs, chrashed, index, size):
    num = 0
    for i in X:
        for j in obs[0]:
            if i[index][0] > j[0] and i[index][0] < j[0]+size and i[index][1] > j[1] and i[index][1] < j[1]+5:
                chrashed[num] = [True, index]
        for k in obs[1]:
            if i[index][0] > k[0] and i[index][0] < k[0] + 5 and i[index][1] > k[1] and i[index][1] < k[1] + size:
                chrashed[num] = [True, index]
        num+=1

def collisionFood(X, ate, index, food, eaten):
    num = 0
    for i in X:
        if i[index][0] > food[0] and i[index][0] < food[0] + 20 and i[index][1] > food[1] and i[index][1] < food[1] + 20:
            ate[num] = [True, index]
        num+=1

    return eaten


#DRAWINGS
