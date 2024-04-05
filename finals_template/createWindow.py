from tkinter import *

windowHeight = 500
windowWidth = 500

# Initializing tkinter window-------------------------------------

window=Tk()
window.title("Window")
window.geometry(f"{windowWidth}x{windowHeight}")
canvas = Canvas(window, width=windowWidth, height=windowHeight, bg="white")
canvas.grid()



def draw_rectangle(x, y, width, height, color): # X, Y --> UPPER-LEFT corner of the rectangle
    canvas.create_rectangle(x, y, (x+width), (y+height), fill=color, outline="black")


def draw_circle(x, y, radius, color): # X, Y --> CENTER of the circle
    canvas.create_oval(x-radius, y-radius, x+radius, y+radius, fill=color)


def draw_text(x, y, t, fontSize): # X, Y --> CENTER coordinates   t --> your text
    canvas.create_text(x, y, text=t, fill="black", font=('Helvetica %s bold', fontSize))

