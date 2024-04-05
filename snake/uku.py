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
x_pos = 1
y_pos = 0
x_apple = 0
y_apple = 0
snake_body = [[]]
snake_tail= False


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

def close():
    window.destroy()

def create_snake():
    global snake_body, snake_tail
    if not snake_tail:
        snake_body.pop(0)
        snake_body.append([x_head, y_head])
    else:
        snake_body.append([x_head, y_head])
        snake_tail = False
    
    for part in snake_body:
        x_cor, y_cor = part
        canvas.create_rectangle(x_cor, y_cor, (x_cor+block_size), (y_cor+block_size), fill="green", outline="black")

def check_snake_collisions():
    global x_head, y_head, snake_body
    
    if [x_head, y_head] in snake_body:
        close()

def snake_move():
    global x_head, y_head, snake_tail

    x_head = x_head + (x_pos*block_size)
    y_head = y_head + (y_pos*block_size)
    check_snake_collisions()
    if 0 - block_size < x_head < window_width + block_size and 0 - block_size < y_head < window_height + block_size:
        create_snake()
        sleep(.1)
    else:
        close()

def snake_update():
    global x_head, y_head, apple, score, snake_tail
    create_apple(apple)
    snake_move()
    if x_head == x_apple and y_head == y_apple:
        print("Hei! U got apple!")
        score += 10
        print(f"Score: {score}")
        apple = True
        snake_tail = True

def create_apple(create):
    global x_apple, y_apple, apple
    if create:
        x_apple = randrange(start=0, stop=window_width, step=block_size) - 10
        y_apple = randrange(start=0, stop=window_height, step=block_size) - 10
        apple = False
    canvas.create_rectangle(x_apple, y_apple, (x_apple+block_size), (y_apple+block_size), fill="red", outline="black")
    sleep(.1)

def main():
    global canvas
    window.title("Snake")
    window.geometry(f"{window_height}x{window_width}")
    canvas = Canvas(window, width=window_width, height=window_height, bg="gray50")
    canvas.grid()
    window.bind('<Key>', key_input)
    while(snake_go):
        canvas.delete("all")

        snake_update()

        window.update()
        
if __name__ == "__main__":
    main()
