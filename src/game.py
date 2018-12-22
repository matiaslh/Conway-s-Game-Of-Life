import tkinter as tk
import numpy as np

N, M = 50, 50
grid = np.full((N, M), False)
root, canvas, entry = None, None, None
time_interval = 400
colours = {'off': 'light grey', 'on': 'blue'}

def isAlive(curr_state, neighbours):
    if curr_state and (neighbours == 2 or neighbours == 3):
        return True
    elif not curr_state and neighbours == 3:
        return True
    return False

def getNeighbours(i, j):
    global grid
    count = 0
    for x_offset in range(-1, 2):
        for y_offset in range(-1, 2):
            x = (i + x_offset) % len(grid)
            y = (j + y_offset) % len(grid[i])
            square = grid[x][y]
            if not (x_offset == 0 and y_offset == 0) and square:
                count += 1
    return count

def run_gen():
    global grid
    new_grid = np.full((N, M), False)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            neighbours = getNeighbours(i, j)
            boo = isAlive(grid[i][j], neighbours)
            new_grid[i][j] = boo
    grid = new_grid
    drawGrid()

def run_forever():
    global root, time_interval
    root.after(time_interval, run_forever)
    run_gen()

def mouse_clicked(event):
    global grid, canvas, colours

    if canvas.find_withtag(tk.CURRENT):
        item_id = canvas.find_withtag(tk.CURRENT)[0]
        i = (item_id - 1) // N
        j = (item_id - 1) % N
        
        grid[i][j] = not grid[i][j]
        canvas.itemconfig(tk.CURRENT, fill=colours['on'] if grid[i][j] else colours['off'])

def drawGrid():
    global grid, canvas, colours
    ids = canvas.find('all')

    for id in ids:
        i = (id - 1) // N
        j = (id - 1) % N
        canvas.itemconfig(id, fill=colours['on'] if grid[i][j] else colours['off'])

def change_interval():
    global time_interval, entry
    time_interval = entry.get()

