from time import sleep
from math import floor, ceil # need on ümardamiseks kasulikud
from random import randint, choice # choice on väga kasulik, kui on vaja valida suvaline element listist
from ReadOrWrite import readFromFile, writeToFile # readFromFile(line_number) / writeToFile(text, line_number)
from tkinter import *
from PIL import Image,ImageTk


windowHeight = 800
windowWidth = 1000
tile_size = 25


# Initializing tkinter window-------------------------------------

window=Tk()
canvas = Canvas(window, width=windowWidth, height=windowHeight, bg="white")
img= ImageTk.PhotoImage(Image.open("map/map.png"))
canvas.create_image(0,0,anchor=NW,image=img)
canvas.pack(fill=BOTH, expand=YES)

grid_width = windowWidth // tile_size
grid_height = windowHeight // tile_size
window.title("Window")
window.geometry(f"{windowWidth}x{windowHeight}")


stopped = False # the ending condition for the whole program
window.protocol("WM_DELETE_WINDOW", lambda: globals().update({'stopped': True})) 


lineNum = 0

def draw_circle(x, y, radius, color): # X, Y --> CENTER of the circle
    canvas.create_oval(x-radius, y-radius, x+radius, y+radius, fill=color)


def getCoordinates(event):
    global lineNum
    x = event.x
    y = event.y

    data = ""
    data = (str(x) + ", " + str(y) + "\n")


    draw_circle(x, y, 1, "red")

    filename = 'map/saveFile.txt'

    with open(filename, 'a') as file:
            file.write(data) 
            
    lineNum += 1
    






#canvas.bind('<ButtonPress-1>', lambda event: canvas.scan_mark(event.x, event.y))
#canvas.bind("<B1-Motion>", lambda event: canvas.scan_dragto(event.x, event.y, gain=1))
canvas.bind("<ButtonPress-1>", getCoordinates)
#canvas.bind("<B1-Motion>", scroll_move)


while (stopped == False):
    sleep(0.01)


    window.update()