from tkinter import *
from time import sleep

window = Tk()
window_width = 500
window_height = 500
snake_go = True
block_size = 20
game_map = []
x_head = window_width // 2
y_head = window_height // 2
x_pos = 0
y_pos = 0


def arrow_right(event):
    global x_pos, y_pos

    x_pos = 1
    y_pos = 0

def arrow_left(event):
    global x_pos, y_pos

    x_pos = -1
    y_pos = 0

def arrow_up(event):
    global y_pos, x_pos

    y_pos = -1
    x_pos = 0

def arrow_down(event):
    global y_pos, x_pos

    y_pos = 1
    x_pos = 0

def close(event):
    window.destroy()

window.bind('<Right>', arrow_right)
window.bind('<Left>', arrow_left)
window.bind('<Up>', arrow_up)
window.bind('<Down>', arrow_down)
window.bind('<Escape>', close)

def create_snake(x1: int = 0, y1: int = 0):
    canvas.create_rectangle(x1, y1, (x1+block_size), (y1+block_size), fill="green", outline="black")

def snake_move():
    global x_head, y_head

    x_head = x_head + (x_pos*block_size)
    y_head = y_head + (y_pos*block_size)
    if 0 < x_head < window_width and 0 < y_head < window_height:
        create_snake(x_head, y_head)
        sleep(.3)
    else:
        close()

def screen_update():
    pass


window.title("Snake")
window.geometry(f"{window_height}x{window_width}")
canvas = Canvas(window, width=window_width, height=window_height, bg="gray50")
canvas.grid()

row = []
for i in range(window_height // block_size):
    for j in range(window_width // block_size):
        row.append(0)
    game_map.append(row)
    row = []

def main():
    while(snake_go):
        canvas.delete("all")

        snake_move()

        window.update()
        pass
        
        

if __name__ == "__main__":
    main()
