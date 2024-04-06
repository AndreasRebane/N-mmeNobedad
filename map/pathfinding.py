from time import sleep
from math import floor, ceil, sqrt # need on ümardamiseks kasulikud
from random import randint, choice # choice on väga kasulik, kui on vaja valida suvaline element listist
from ReadOrWrite import readFromFile, writeToFile # readFromFile(line_number) / writeToFile(text, line_number)
from tkinter import *
from PIL import Image,ImageTk
import re


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
startPos = []
endPos = []
coordinates = []



def readCoordinatesFromFile():
    with open("map/coords.txt", 'r') as file: 
        data = file.readlines()

    for line in data:
        clean = line.split(", ")

        coordinates.append([int(clean[0]), int(clean[1])])

    print(len(coordinates))

def findPathCoords():
    pathCoords = []
    keepSearching = True
    temp_coordinate =[] 

    
    for coord in coordinates:
        len = sqrt((coord[0] - startPos[0])**2 + (coord[1] - startPos[1])**2)
        if len < 10: #this dumb, me fix later (possible no coords fount -> big bad)
            pathCoords.append[coord]

    for pathCoord in pathCoords:
                len = sqrt((pathCoord[0] - endPos[0])**2 + (pathCoord[1] - endPos[1])**2)

                if len < lastLen:
                    temp_coordinate = pathCoord
                    lastLen = len


    lastLen = 0
    coordinate = endPos

    while(keepSearching == True):

        for pathCoord in pathCoords:
            len = sqrt((pathCoord[0] - coordinate[0])**2 + (pathCoord[1] - coordinate[1])**2)

            if len < lastLen:
                temp_coordinate = pathCoord
                lastLen = len




def draw_circle(x, y, radius, color): # X, Y --> CENTER of the circle
    canvas.create_oval(x-radius, y-radius, x+radius, y+radius, fill=color)


def getCoordinates(event):
    global lineNum, startPos, endPos
    x = event.x
    y = event.y


    draw_circle(x, y, 1, "red")

    match(lineNum):
        case 0:
            startPos = [event.x, event.y]
            print(startPos)
        case 1:
            endPos = [event.x, event.y]
            print(endPos)
            findPathCoords()
            
    lineNum += 1
    






#canvas.bind('<ButtonPress-1>', lambda event: canvas.scan_mark(event.x, event.y))
#canvas.bind("<B1-Motion>", lambda event: canvas.scan_dragto(event.x, event.y, gain=1))
canvas.bind("<ButtonPress-1>", getCoordinates)
#canvas.bind("<B1-Motion>", scroll_move)



readCoordinatesFromFile()

while (stopped == False):
    sleep(0.01)


    window.update()