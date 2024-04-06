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
    global isSufficientPathFound
    totalPathUsedCordinates: list = []
    nextStepPoint: list = []
    closestEndPoints: list = []
    distance: int = 0
    lastPointDistance: int = 2000000

    # Render start and end positions
    draw_circle(startPos[0], startPos[1], 5, "Green")
    draw_circle(endPos[0], endPos[1], 5, "Yellow")
    window.update()

    # Finds closest end points
    while (len(closestEndPoints) < 3):
            distance += 3
            for coord in coordinates:
                lengthS = sqrt((coord[0] - endPos[0])**2 + (coord[1] - endPos[1])**2)
                if (lengthS < distance):
                    closestEndPoints.append(coord)
    print(closestEndPoints)

    sleep(2)

    nextStepPoint = startPos
    # Render path
    isSufficientPathFound = 0
    while isSufficientPathFound == 0:
        sleep(0.2)
        distance = 0
        closestPoints = []
        # get a few cordinates and increse range if needed
        while (len(closestPoints) < 8):
            distance += 5

            # Take and process every cordinate
            for coord in coordinates:
                lengthS = sqrt((coord[0] - nextStepPoint[0])**2 + (coord[1] - nextStepPoint[1])**2)

                if (lengthS < distance):
                    try:
                        totalPathUsedCordinates.index(coord)
                    except:
                        closestPoints.append(coord)

        if (len(closestPoints) == 0):
            closestPointSum += 1
            closestPoints = nextStepPoint


        closestPointSum: int = 20000000 # large value
        closestPoint: list = []
        for x in closestPoints:
            lengthE = sqrt((x[0] - endPos[0])**2 + (x[1] - endPos[1])**2)
            if (lengthE < closestPointSum):
                closestPointSum = lengthE
                closestPoint = x

        # Render the point and add it to used points list
        totalPathUsedCordinates.append(closestPoint)
        nextStepPoint = closestPoint
        
        try:
            draw_circle(closestPoint[0], closestPoint[1], 2, "red")
        except:
            s = 1
        window.update()

        for x in closestEndPoints:
            try:
                totalPathUsedCordinates.index(x)
                isSufficientPathFound == 1
                print("Sufficient path found")
                return
            except:
                bla = 0




        
        #for pathCoord in pathCoords:
        #            length = sqrt((pathCoord[0] - endPos[0])**2 + (pathCoord[1] - endPos[1])**2)
#
        #            if length < lastLen:
      #                  startPos = pathCoord
       #                 draw_circle(startPos[0], startPos[1], 2, "red")
       #                 window.update()
       #                 lastLen = length

        #pathCoords = []
        #lastLen = 99999
        #xx = 1




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
