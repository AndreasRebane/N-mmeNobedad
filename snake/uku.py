from tkinter import *
from time import sleep

window = Tk()
window_height = 500
window_width = 500
snake_go = True
block_size = 20
game_map = []

def create_snake(x1: int = 100, y1: int = 100):
    canvas.create_rectangle(x1, y1, (x1+block_size), (y1+block_size), fill="green", outline="black")

def snake_move():
    pass

def screen_update():
    pass


window.title("Snake")
window.geometry(f"{window_height}x{window_width}")
canvas = Canvas(window, width=window_width, height=window_height, bg="gray50")
canvas.grid()

def main():
    while(snake_go):
        canvas.delete("all")

        create_snake()

        window.update()
        pass
        
        

if __name__ == "__main__":
    main()
