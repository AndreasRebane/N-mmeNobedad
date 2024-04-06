from time import sleep
from math import floor, ceil # need on ümardamiseks kasulikud
from random import randint, choice # choice on väga kasulik, kui on vaja valida suvaline element listist
from ReadOrWrite import readFromFile, writeToFile # readFromFile(line_number) / writeToFile(text, line_number)
from tkinter import *
from PIL import ImageTk


windowHeight = 500
windowWidth = 800
tile_size = 25


# Initializing tkinter window-------------------------------------

window=Tk()
canvas = Canvas(window, width=windowWidth, height=windowHeight, bg="white")

grid_width = windowWidth // tile_size
grid_height = windowHeight // tile_size
window.title("Window")
window.geometry(f"{windowWidth}x{windowHeight}")


stopped = False # the ending condition for the whole program
window.protocol("WM_DELETE_WINDOW", lambda: globals().update({'stopped': True})) 



class Table:

    def __init__(self, data):

        total_rows = len(data)
        total_columns = len(data[0])

        for row in range(total_rows):
            for collumn in range(total_columns):
                 
                width = 10
                self.entry = Entry(canvas, width=width, fg='blue', font=('Arial',16,'bold'))
                 
                self.entry.grid(row=row, column=collumn)
                self.entry.insert(END, data[row][collumn])



def draw_rectangle(x, y, width, height, color): # X, Y --> UPPER-LEFT corner of the rectangle
    canvas.create_rectangle(x, y, (x+width), (y+height), fill=color, outline="black")


def draw_circle(x, y, radius, color): # X, Y --> CENTER of the circle
    canvas.create_oval(x-radius, y-radius, x+radius, y+radius, fill=color)


def draw_text(x, y, t, fontSize): # X, Y --> CENTER coordinates   t --> your text
    canvas.create_text(x, y, text=t, fill="black", font=('Helvetica %s bold', fontSize))



def scroll_start(event):
    canvas.scan_mark(event.x, event.y)


def scroll_move(event):
    canvas.scan_dragto(event.x, event.y, gain=1)


def do_zoom(event):
    x = canvas.canvasx(event.x)
    y = canvas.canvasy(event.y)
    factor = 1.001 ** event.delta
    canvas.scale(ALL, x, y, factor, factor)


canvas.bind("<MouseWheel>", do_zoom)
canvas.bind('<ButtonPress-1>', lambda event: canvas.scan_mark(event.x, event.y))
canvas.bind("<B1-Motion>", lambda event: canvas.scan_dragto(event.x, event.y, gain=1))
canvas.bind("<ButtonPress-1>", scroll_start)
canvas.bind("<B1-Motion>", scroll_move)

img= PhotoImage(file='finals_template/amogus.png', master= canvas)
img_label= Label(canvas,image=img)


while (stopped == False):
    canvas.delete("all")
    sleep(0.01)

    #data = [("Rebane", "12", "13", "sandworm"), ("Uku", "12", "13", "bookworm")]
    #table = Table(data)
    #Some examples:
    #draw_rectangle(0, 0, 100, 100, "blue")
    draw_circle(120, 150, 20, "red")
    #draw_text(120, 180, "Näide", 20)

    #img_label.place(x=0, y=0)

    canvas.grid(columnspan=grid_height, rowspan=grid_width)
    window.update()