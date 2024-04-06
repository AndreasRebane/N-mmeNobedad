from time import sleep
from math import floor, ceil # need on ümardamiseks kasulikud
from random import randint, choice # choice on väga kasulik, kui on vaja valida suvaline element listist
from ReadOrWrite import readFromFile, writeToFile # readFromFile(line_number) / writeToFile(text, line_number)
from createWindow import *

create_window()
stopped = False # the ending condition for the whole program
#Added this so closing the window doesn't crash the program
window.protocol("WM_DELETE_WINDOW", lambda: globals().update({'stopped': True})) 




while (stopped == False):
    canvas.delete("all")
    sleep(0.1)

    #data = [("Rebane", "12", "13", "sandworm"), ("Uku", "12", "13", "bookworm")]
    #table = Table(data)
    #updateWindow()
    #Some examples:
    #draw_rectangle(0, 0, 100, 100, "blue")
    #draw_circle(120, 150, 20, "red")
    #draw_text(120, 180, "Näide", 20)









    
    updateWindow()