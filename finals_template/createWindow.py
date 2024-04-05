from tkinter import *

# Initializing tkinter window-------------------------------------
window=Tk()
canvas=Canvas()
def create_window(windowHeight: int = 500, windowWidth: int = 800, tile_size: int = 25):
    global window, canvas

    grid_width = windowWidth // tile_size
    grid_height = windowHeight // tile_size
    window.title("Window")
    window.geometry(f"{windowWidth}x{windowHeight}")
    canvas = Canvas(window, width=windowWidth, height=windowHeight, bg="white")
    canvas.grid(columnspan=grid_height, rowspan=grid_width)


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

def updateWindow():
    window.update()


