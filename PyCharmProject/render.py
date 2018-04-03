from tkinter import *
import random
import time
from datetime import datetime
from settings import *

def rendera(index, width, height, tk, canvas, X, food, obs, size, chrashed, ate, eaten):
    while index < len(X[1]):
        canvas.delete("all")

        canvas.create_oval(food[0], food[1], food[0] + 20, food[1] + 20, fill="brown")
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
            if chrashed[num][0] == False and ate[num][0] == False:
                if index < len(i):
                    x0 = i[index][0]
                    y0 = i[index][1]
                    x1 = x0+5
                    y1 = y0+5
                canvas.create_rectangle(x0, y0, x1, y1, fill="red")
            elif chrashed[num][0] == False and ate[num][1] >= index:
                if index < len(i):
                    x0 = i[index][0]
                    y0 = i[index][1]
                    x1 = x0+5
                    y1 = y0+5
                canvas.create_rectangle(x0, y0, x1, y1, fill="red")
            elif chrashed[num][1] >= index:
                if index < len(i):
                    x0 = i[index][0]
                    y0 = i[index][1]
                    x1 = x0+5
                    y1 = y0+5
                canvas.create_rectangle(x0, y0, x1, y1, fill="red")

            num += 1
        tk.update()
        time.sleep(0.01)
        index += drawEveryNFrames

    return eaten



#DRAWINGS
