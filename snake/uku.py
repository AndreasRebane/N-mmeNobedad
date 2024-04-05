from tkinter import *
from time import sleep
from random import randrange

window = Tk()
window_width = 500
window_height = 500
snake_go = True
block_size = 20
score = 0
apple = True
x_head = window_width // 2
y_head = window_height // 2
x_pos = 0
y_pos = 0
x_apple = 0
y_apple = 0


def key_input(event):
    global x_pos, y_pos
    if event.keysym == "Right":
        x_pos = 1
        y_pos = 0
    elif event.keysym == "Left":
        x_pos = -1
        y_pos = 0
    elif event.keysym == "Up":
        x_pos = 0
        y_pos = -1
    elif event.keysym == "Down":
        x_pos = 0
        y_pos = 1
    elif event.keysym == "Escape":
        close()
    
window.bind('<Key>', key_input)

def close():
    window.destroy()

def create_snake(x1: int = 0, y1: int = 0):
    canvas.create_rectangle(x1, y1, (x1+block_size), (y1+block_size), fill="green", outline="black")

def snake_move():
    global x_head, y_head

    x_head = x_head + (x_pos*block_size)
    y_head = y_head + (y_pos*block_size)
    if 0 - block_size < x_head < window_width + block_size and 0 - block_size < y_head < window_height + block_size:
        create_snake(x_head, y_head)
        sleep(.1)
    else:
        close()

def snake_update():
    global x_head, y_head, apple, score
    create_apple(apple)
    snake_move()
    if x_head == x_apple and y_head == y_apple:
        print("Hei! U got apple!")
        score += 10
        print(f"Score: {score}")
        apple = True


def create_apple(create):
    global x_apple, y_apple, apple
    if create:
        x_apple = randrange(start=0, stop=window_width, step=block_size) - 10
        y_apple = randrange(start=0, stop=window_height, step=block_size) - 10
        apple = False
    canvas.create_rectangle(x_apple, y_apple, (x_apple+block_size), (y_apple+block_size), fill="red", outline="black")
    sleep(.1)
    

window.title("Snake")
window.geometry(f"{window_height}x{window_width}")
canvas = Canvas(window, width=window_width, height=window_height, bg="gray50")
canvas.grid()

def main():
    while(snake_go):
        canvas.delete("all")

        snake_update()

        window.update()
        pass
        
        

if __name__ == "__main__":
    main()
