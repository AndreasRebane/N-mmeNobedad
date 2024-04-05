from time import sleep
from math import floor, ceil # need on ümardamiseks kasulikud
from random import randint, choice # choice on väga kasulik, kui on vaja valida suvaline element listist
from ReadOrWrite import readFromFile, writeToFile # readFromFile(line_number) / writeToFile(text, line_number)
from createWindow import draw_circle, draw_rectangle, draw_text, window, canvas, button, updateWindow


stopped = False # the ending condition for the whole program



#Added this so closing the window doesn't crash the program
window.protocol("WM_DELETE_WINDOW", lambda: globals().update({'stopped': True})) 

b = button(0, 0, 20, 10, "red")

while (stopped == False): # stopped is just an arbitrary ending condition
    canvas.delete("all")
    sleep(0.1)



    #Some examples:
    draw_rectangle(0, 0, 50, 50, "blue")
    draw_circle(120, 150, 20, "red")
    draw_text(120, 180, "Näide", 20)

    b.place()

    if(b.pressed == True):
        print("pressed")


    
 
    updateWindow()