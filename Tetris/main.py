from tkinter import *
import time
from math import floor
from random import randint, choice


"""
Hello!

Welcome to this ugly mess that is my code.

sorry in advance..


To do:
Make blocks rotate
Add a title screen
Add an ending screen
Add a score system
Add an options menu for changing grid size, gamespeed and window resolution (maybe..?)
Fix blocks sometimes getting destroyed when moving against the left border
And Optimize :(
"""


blocks_in_row = 10 # the actual grid dimentions (default size = 10x20)
blocks_in_collumn = 24
block_size = 30 # edge length in pixels - determines the size of the application window
gameover = False

window_height = blocks_in_collumn * block_size
window_width = blocks_in_row * block_size


window=Tk()
window.title("T3TRIS")
window.geometry(str(window_width) + "x" + str(window_height))
canvas = Canvas(window, width=window_width, height=window_height, bg="gray5")
canvas.grid()



# All the seven shapes of the original game + a special surprise - the color of the individual blocks should also be included somewhere
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
# btw I'm creating 2 lists - one keeps track of dynamic blocks - other keeps track of static blocks

keeping_track_of_blocks = []
keeping_track_of_static_blocks = []
for i in range(blocks_in_collumn):
    keeping_track_of_blocks.append([])
    keeping_track_of_static_blocks.append([])
        
    for u in range(blocks_in_row):
        keeping_track_of_blocks[i].append(0)
        keeping_track_of_static_blocks[i].append(0)
    #print(keeping_track_of_blocks[i])
    
empty_row = keeping_track_of_static_blocks[0] # simply saving one empty row for later use
waiting_for_keyboard_input = True
spawn_next_block = False
falling_speed = 5
falling_counter = 0



def debug():
    print("\n")
    for i in range(blocks_in_collumn):
        print("")
        print(keeping_track_of_blocks[i], end="")
        #print(keeping_track_of_static_blocks[i], end="")


def draw_rectangle(row_index, collumn_index):
    x1 = block_size * collumn_index
    y1 = block_size * row_index

    canvas.create_rectangle(x1, y1, (x1+block_size), (y1+block_size), fill="red", outline="black")


def left_right_movement(direction):
    global falling_counter

    falling_counter = 0
    
    if direction == "left":
        if left_movement_is_blocked == False:       
            for i in range(blocks_in_collumn):
                keeping_track_of_blocks[i].insert(blocks_in_row, 0)
                del keeping_track_of_blocks[i][0]
        #debug()
            

    if direction == "right":
        if right_movement_is_blocked == False:
            for i in range(blocks_in_collumn):
                keeping_track_of_blocks[i].insert(0, 0)
                del keeping_track_of_blocks[i][blocks_in_row]
        #debug()
"""
def block_rotation(direction):
    for i in range(blocks_in_collumns):
        for u in range(blocks_in_rows):
            if ...
    
    if direction == "clockwise":
"""        
            

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


def merge_lists():
    for i in range(blocks_in_collumn):
        for u in range(blocks_in_row):
            keeping_track_of_static_blocks[i][u] += keeping_track_of_blocks[i][u]
            keeping_track_of_blocks[i][u] = 0
    

def update(): # So inefficient that it's embarrassing - looking through every cell like 3 times in 1 cycle X(
    global waiting_for_keyboard_input, spawn_next_block, right_movement_is_blocked, left_movement_is_blocked, keeping_track_of_blocks, falling_counter, gameover
    
    canvas.delete("all")
    canvas.create_rectangle(0, 4*block_size, blocks_in_row*block_size, 0, fill="gray10", outline="gray80")

    if falling_counter == falling_speed:
        falling_counter = 0
        keeping_track_of_blocks = [empty_row[:]] + keeping_track_of_blocks # Can't put into words how much shit forgetting this caused --> [:]
        del keeping_track_of_blocks[-1]
    else:
        falling_counter += 1


    if spawn_next_block == True:
        spawn_next_block = False
        block = choice(blocks) #picks a random block
        startpoint = randint(0, blocks_in_row-len(block[0]))
        #print(startpoint, len(block[0]))

        for i in range(len(block)):
            index_count = 0
            for element in block[i]:
                keeping_track_of_blocks[i][startpoint + index_count] = element
                index_count += 1


    left_movement_is_blocked = False
    right_movement_is_blocked = False
    for i in range(blocks_in_collumn):
        for u in range(blocks_in_row):
            if(keeping_track_of_static_blocks[i][u] == 1):
                draw_rectangle(i, u)
                if i <= 4:
                    print("Game Over! wah wah")
                    gameover = True    

            if(keeping_track_of_blocks[i][u] == 1):
                draw_rectangle(i, u)

                if u-1 < 0 or keeping_track_of_static_blocks[i][u-1] == 1:
                    left_movement_is_blocked = True
                if u+1 >= blocks_in_row or keeping_track_of_static_blocks[i][u+1] == 1:
                    right_movement_is_blocked = True

                if(i+1 >= blocks_in_collumn or keeping_track_of_static_blocks[i+1][u] == 1):
                    merge_lists()
                    waiting_for_keyboard_input = True
                    #debug()


    
while not gameover:
    time.sleep(0.05)

    window.bind("<Key>", keyboard_input)

    update()
    window.update()
