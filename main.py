import sys
import tkinter as tk
import game

def createGrid(container):

    canvas = tk.Canvas(container, bg='light grey')
    canvas.place_configure(relwidth=1, relheight=1)
    canvas.bind('<Button-1>', game.mouse_clicked)
    canvas.update()

    width, height = canvas.winfo_width(), canvas.winfo_height()

    x_length = (width // game.N)
    y_length = (height // game.M)

    for i in range(game.N):
        for j in range(game.M):
            rect = canvas.create_rectangle(i * x_length, j * y_length, (i+1) * x_length, (j+1) * y_length)
            game.squares[i][j] = rect


########################
# Initialize the window
########################

root = tk.Tk()
root.title('Game of Life')

# Set window to fullscreen mode, escape to quit
root.attributes('-fullscreen', True)
root.bind("<Escape>", lambda e: root.quit())


# Make the canvas with the main grid
frame = tk.Frame(root)

frame.place_configure(relx=1/10, relwidth=0.8, relheight=0.8)

frame.update()
createGrid(frame)

# Create the window
root.mainloop()


