from tkinter import *

windowHeight = 500
windowWidth = 500



class button:
    list = []

    def on_press(self, event):
        print("aghhhhhhh")
        self.pressed = True

    def on_release(self, event):
        print("aghhhhhhh")
        self.pressed = False

    def __init__(self, x, y, w, h, color):
        self.x = x
        self.y = y
        self.button = Button(window, height=h, width=w, bg=color, image=photoimage)
        self.button.bind("<ButtonPress>", self.on_press)
        self.button.bind("<ButtonRelease>", self.on_release)
        self.pressed = False


    
        button.list.append(self)

    def place(self):
        self.pressed = False
        self.button.place(x=self.x, y=self.y)



# Initializing tkinter window-------------------------------------

window=Tk()
window.title("Window")
window.geometry(f"{windowWidth}x{windowHeight}")
canvas = Canvas(window, width=windowWidth, height=windowHeight, bg="white")
canvas.grid()

photo = PhotoImage("amogus.png") 
photoimage = photo.subsample(3, 3) 

def draw_rectangle(x, y, width, height, color): # X, Y --> UPPER-LEFT corner of the rectangle
    canvas.create_rectangle(x, y, (x+width), (y+height), fill=color, outline="black")


def draw_circle(x, y, radius, color): # X, Y --> CENTER of the circle
    canvas.create_oval(x-radius, y-radius, x+radius, y+radius, fill=color)


def draw_text(x, y, t, fontSize): # X, Y --> CENTER coordinates   t --> your text
    canvas.create_text(x, y, text=t, fill="black", font=('Helvetica %s bold', fontSize))

def updateWindow():
    window.update()


