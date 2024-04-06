from time import sleep
from math import floor, ceil, sqrt # need on ümardamiseks kasulikud
from random import randint, choice # choice on väga kasulik, kui on vaja valida suvaline element listist
from tkinter import *
from PIL import Image,ImageTk


windowHeight = 800
windowWidth = 1000
tile_size = 25


# Initializing tkinter window-------------------------------------


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
    global startPos
    pathCoords = []
    lastLen = 99999

    while startPos != endPos:
        print(startPos)
        #print(endPos)
        for coord in coordinates:
            length = sqrt((coord[0] - startPos[0])**2 + (coord[1] - startPos[1])**2)
            if length < 5: #this dumb, me fix later (possible no coords fount -> big bad)
                pathCoords.append(coord)

        for pathCoord in pathCoords:
                    length = sqrt((pathCoord[0] - endPos[0])**2 + (pathCoord[1] - endPos[1])**2)

                    if length < lastLen:
                        startPos = pathCoord
                        draw_circle(startPos[0], startPos[1], 2, "red")
                        window.update()
                        lastLen = length

        pathCoords = []
        lastLen = 99999




def draw_circle(x, y, radius, color): # X, Y --> CENTER of the circle
    canvas.create_oval(x-radius, y-radius, x+radius, y+radius, fill=color)




def draw_path(_startX, _startY, _endX, _endY):
    global window, canvas

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


    global startPos, endPos

    startPos = [_startX, _startY]
    endPos = [_endX, _endY]

    readCoordinatesFromFile()
    findPathCoords()

    while (stopped == False):
        sleep(0.01)


        window.update()
