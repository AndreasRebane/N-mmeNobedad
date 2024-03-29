from tkinter import *
import time
from math import floor
from random import randint, choice


"""
Hello!

Welcome to this ugly mess that is my code.

sorry in advance..


To do:
Add a small delay between when blocks hit the floor and when they can't be moved anymore
Add a score system
Add an options menu - for changing gamesize, gamespeed and window resolution
"""


blocks_in_row = 10 #the game grid dimentions
blocks_in_collumn = 24
block_size = 30 # determines the size of the application window
gameover = False
rows_destroyed = 0
blocks_deployed = 0
windowtype = "titlescreen"

window_height = blocks_in_collumn * block_size
window_width = blocks_in_row * block_size


window=Tk()
window.title("T3TRIS")
window.geometry(str(window_width) + "x" + str(window_height))
canvas = Canvas(window, width=window_width, height=window_height, bg="gray5")
canvas.grid()



# All the seven shapes of the original game - the color of the individual blocks should also be included somewhere
t_block = [ [0, 1, 0],
            [1, 1, 1],
            [0, 0, 0]]

j_block = [ [1, 0, 0],
            [1, 1, 1],
            [0, 0, 0]]

l_block = [ [0, 0, 1],
            [1, 1, 1],
            [0, 0, 0]]

o_block = [ [0, 1, 1],
            [0, 1, 1],
            [0, 0, 0]]

s_block = [ [0, 1, 1],
            [1, 1, 0],
            [0, 0, 0]]

z_block = [ [1, 1, 0],
            [0, 1, 1],
            [0, 0, 0]]

i_block = [ [0, 0, 0, 0],
            [1, 1, 1, 1],
            [0, 0, 0, 0],
            [0, 0, 0, 0]]

a_block = [ [0, 1, 1, 1],
            [1, 1, 1, 0],
            [1, 1, 1, 0],
            [0, 1, 1, 1],
            [0, 1, 1, 1],
            [0, 1, 0, 1]]

blocks = [t_block, j_block, l_block, o_block, s_block, z_block, i_block]
# blocks = [a_block] # Enable this for some fun

# This is pretty ugly - there must be a better way for populating lists...

keeping_track_of_static_blocks = []
for i in range(blocks_in_collumn):
    keeping_track_of_static_blocks.append([])     
    for u in range(blocks_in_row):
        keeping_track_of_static_blocks[i].append(0)
    
empty_row = keeping_track_of_static_blocks[0]
waiting_for_keyboard_input = True
spawn_next_block = False
falling_speed = 5
falling_counter = 0



def debug():
    print("\n")
    for i in range(blocks_in_collumn):
        print("")
        print(keeping_track_of_static_blocks[i], end="")


def draw_rectangle(row_index, collumn_index):
    x1 = block_size * collumn_index
    y1 = block_size * row_index

    canvas.create_rectangle(x1, y1, (x1+block_size), (y1+block_size), fill="red", outline="black")


block_row = 0
block_collumn = 0
block = []


def left_right_movement(direction):
    global falling_counter, block_row

    falling_counter = 0
    
    if direction == "left":
        if left_movement_is_blocked == False:
            block_row -= 1            

    if direction == "right":
        if right_movement_is_blocked == False:
            block_row += 1
            

def draw_blocks():
    global waiting_for_keyboard_input, left_movement_is_blocked, right_movement_is_blocked, gameover, windowtype

    left_movement_is_blocked = False
    right_movement_is_blocked = False
    
    for i in range(blocks_in_collumn):
        for u in range(blocks_in_row):
            if(keeping_track_of_static_blocks[i][u] == 1):
                draw_rectangle(i, u)
                if i <= 4:
                    gameover = True
                    windowtype = "titlescreen"
                    waiting_for_keyboard_input = True
                

    for i in range(len(block)):
        for u in range(len(block[i])):
            if(block[i][u] == 1):
                draw_rectangle(block_collumn+i, block_row+u)


                if block_row + u-1 < 0 or keeping_track_of_static_blocks[block_collumn+i][block_row+u-1] == 1:
                    left_movement_is_blocked = True
                if block_row + u+1 >= blocks_in_row or keeping_track_of_static_blocks[block_collumn+i][block_row+u+1] == 1:
                    right_movement_is_blocked = True

                if(block_collumn + i + 1 >= blocks_in_collumn or keeping_track_of_static_blocks[block_collumn+i+1][block_row+u] == 1):
                    merge_lists()
                    waiting_for_keyboard_input = True


def rotate_block(direction):
    global block, block_row

    temp_list = list(map(list, block))
    
    if direction == "clockwise":
        for i in range(len(block)):
            for u in range(len(block[i])):
                temp_list[i][u] = block[len(block[i])-u-1][i]
    elif direction == "counterclockwise":
        for i in range(len(block)):
            for u in range(len(block[i])):
                temp_list[i][u] = block[u][len(block[i])-i-1]

    x = 0
    if(block_row < 0):
        x = 1
    elif(block_row + u > len(keeping_track_of_static_blocks[0])-1):
        x = -1


    can_rotate = True
    for i in range(len(temp_list)):
        for u in range(len(temp_list[i])):
            if(temp_list[i][u] == 1 and keeping_track_of_static_blocks[block_collumn + i][block_row + u + x] == 1):
                can_rotate = False
                x = 0
                
    block_row += x
    if can_rotate:
        block = list(map(list, temp_list))


def destroy_rows():
    global keeping_track_of_static_blocks, rows_destroyed
      
    for i in range(blocks_in_collumn):
        count = 0
        for u in range(blocks_in_row):
            if(keeping_track_of_static_blocks[i][u] == 1):
                count += 1
            else:
                count = 0
        if count == blocks_in_row:
            del keeping_track_of_static_blocks[i]
            keeping_track_of_static_blocks = [empty_row[:]] + keeping_track_of_static_blocks #Can't put into words how much shit forgetting this caused --> [:]
            rows_destroyed += 1
    
def keyboard_input(event):
    global waiting_for_keyboard_input, spawn_next_block, falling_counter
    #print(event.char, event.keysym, event.keycode)
    #print(event.keysym)
    match event.keysym:
        case "space":
            if waiting_for_keyboard_input == True:
                waiting_for_keyboard_input = False
                spawn_next_block = True
        case "Left":
            left_right_movement("left")
        case "Right":
            left_right_movement("right")
        case "Down":
            falling_counter = falling_speed
        #case "Up":
        #    debug()
        case "a":
            rotate_block("counterclockwise")

        case "d":
            rotate_block("clockwise")


def merge_lists():
    for i in range(len(block)):
        for u in range(len(block[i])):
            if(block[i][u] == 1):
                keeping_track_of_static_blocks[block_collumn + i][block_row + u] = 1
    destroy_rows()
    

   

def update():
    global spawn_next_block, falling_counter, block, block_row, block_collumn, blocks_deployed
    
    canvas.delete("all")
    canvas.create_rectangle(0, 4*block_size, blocks_in_row*block_size, 0, fill="gray10", outline="gray80")

    if falling_counter == falling_speed:
        falling_counter = 0
        block_collumn += 1
    else:
        falling_counter += 1


    if spawn_next_block == True:
        spawn_next_block = False
        blocks_deployed += 1
        block = choice(blocks[:]) #picks a random block
        startpoint = randint(0, blocks_in_row-len(block[0]))
        block_row = startpoint
        block_collumn = 0

    draw_blocks()


def switch_window():
    global windowtype

    if blocks_deployed > 0:
        exit()
        
    windowtype = "tetris"

def titlescreen():
    global text, button
    window.unbind("<Key>")

    text = Text(canvas, height = window_height, width = window_width, bg="gray10", fg="white")

    button = Button(canvas, text ="Hello", command = switch_window)
    button.configure(width=20, height=7, bg="red", fg="white")

    if blocks_deployed > 0:
        text.insert(INSERT, "\nWell played! \n")
        text.insert(INSERT, "You used: " + str(blocks_deployed) + " pieces\n")
        text.insert(INSERT, "You destroyed: " + str(rows_destroyed) + " row(s)\n")
        button.configure(text="PRESS HERE TO QUIT")
    else:
        text.insert(INSERT, "\nWelcome to Tetris! \n\n\n\n")
        text.insert(INSERT, "Here's how to play: \n\n")
        text.insert(INSERT, "-Deploy pieces by pressing SPACE \n")
        text.insert(INSERT, "-Move left or right with arrow keys \n")
        text.insert(INSERT, "-Use 'a' & 'd' to rotate \n")
        text.insert(INSERT, "-Hold downwards arrow to fall faster \n\n")
        button.configure(text="PRESS HERE TO START")
    
    button.place(x=window_width/3-20, y=window_height/2)
    text.pack()
    

def gamescreen():
    text.pack_forget()
    button.destroy()
    
    window.bind("<Key>", keyboard_input)
    update()

while True: #bad habbit...
    time.sleep(0.05)

    if gameover:
        windowtype = "titlescreen"
        gameover = False

    if windowtype == "titlescreen":
        waiting_for_keyboard_input = True
        titlescreen()
    elif windowtype == "tetris" or not waiting_for_keyboard_input:
        gamescreen()

    windowtype = ""
    window.update()

