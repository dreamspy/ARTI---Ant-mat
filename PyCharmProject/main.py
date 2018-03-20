from tkinter import *
import random
import time
from datetime import datetime
import numpy as np



def main():
    tk = Tk()
    canvas = Canvas(tk, width=800, height=600)
    canvas.pack()
    width = 800
    height = 600
    index = 0

    while True:
        rendera(index, width, height, tk, canvas, X)


if __name__ == "__main__":
    main()