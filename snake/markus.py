from tkinter import *
from time import sleep
from math import *
from random import randint

xMovement = 0
yMovement = 0
xBlockPos = 0
yBlockPos = 0
xEnemyPos = 0
yEnemyPos = 0


def draw_rectangle(row_index, collumn_index, color):
    x1 = 20 * collumn_index
    y1 = 20 * row_index

    canvas.create_rectangle(x1, y1, (x1+20), (y1+20), fill=color, outline="black")

def movement(event):
    direction = event.keysym
    print(direction)
    global xMovement, yMovement
    if direction == "Left":
        xMovement = -1
        yMovement = 0

    if direction == "Right":
        xMovement = 1
        yMovement = 0

    if direction == "Up":
        yMovement = 1
        xMovement = 0

    if direction == "Down":
        yMovement = -1
        xMovement = 0

def isOutOfBounds():
    global yBlockPos, xBlockPos
        
    if (yBlockPos > 25):
        yBlockPos = 0
    if (yBlockPos < 0):
        yBlockPos = 25
    if (xBlockPos > 25):
        xBlockPos = 0
    if (xBlockPos < 0):
        xBlockPos = 25

def generateEnemy():
    global xEnemyPos, yEnemyPos
    xEnemyPos = randint(0, 25)
    yEnemyPos = randint(0, 25)


def drawEnemy():
    draw_rectangle(xEnemyPos, yEnemyPos, "Green")

def enemyLogic():
    
    print(xEnemyPos, xBlockPos)
    if (xBlockPos == yEnemyPos and yBlockPos == xEnemyPos):
        print("Collision")
        generateEnemy()
        drawEnemy()

        #bigger snake

def main():
    global canvas, window
    window = Tk()
    canvas = Canvas(window, width=500, height=500, bg="gray5")
    canvas.grid()

    window.title("snake")
    window.geometry("500x500")
    
    window.bind("<Key>", movement)

    global xBlockPos, yBlockPos
    xBlockPos = 5
    yBlockPos = 5

    generateEnemy()
    while(True):
        canvas.delete("all")
        xBlockPos += xMovement
        yBlockPos += -yMovement

        print(xBlockPos)

        isOutOfBounds()
        draw_rectangle(yBlockPos, xBlockPos, "Red")

        drawEnemy()
        enemyLogic()
        window.update()
        sleep(0.1)

main()