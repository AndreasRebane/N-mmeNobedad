from tkinter import *
from time import sleep
from math import floor, ceil # need on ümardamiseks kasulikud
from random import randint, choice # choice on väga kasulik, kui on vaja valida suvaline element listist
from ReadOrWrite import readFromFile, WriteToFile # readFromFile(line_number) // writeToFile(text, line_number)


windowHeight = 500
windowWidth = 500

stopped = False # the ending condition for the whole program



# Initializing tkinter window-------------------------------------

window=Tk()
window.title("Window")
window.geometry(f"{windowWidth}x{windowHeight}")
canvas = Canvas(window, width=windowWidth, height=windowHeight, bg="white")
canvas.grid()

def on_close():
    global stop 
    stopped = True
window.protocol("WM_DELETE_WINDOW", on_close) #Added this so closing the window doesn't crash the program

def draw_rectangle(x, y, width, height, color): # X, Y --> UPPER-LEFT corner of the rectangle
    canvas.create_rectangle(x, y, (x+width), (y+height), fill=color, outline="black")

def draw_circle(x, y, radius, color): # X, Y --> CENTER of the circle
    canvas.create_oval(x-radius, y-radius, x+radius, y+radius, fill=color)

def draw_text(x, y, t, fontSize): # X, Y --> CENTER coordinates   t --> your text
    canvas.create_text(x, y, text=t, fill="black", font=('Helvetica %s bold', fontSize))

# Tkinter initialization end -------------------------------------




def draw(): # EVERTHING that needs to be drawn goes in here

    canvas.delete("all")


    #Some examples:
    draw_rectangle(0, 0, 50, 50, "blue")
    draw_circle(120, 150, 20, "red")
    draw_text(120, 180, "Näide", 20)



while (stopped == False): # stop is just some arbitrary game-end condition

    sleep(0.1)



    #your code goes mostly here



    draw()
    window.update()