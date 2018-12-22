import sys
import tkinter as tk
import game

def createGrid(container):

    canvas = tk.Canvas(container)

    game.canvas = canvas

    canvas.place_configure(relwidth=1, relheight=0.9)
    canvas.bind('<Button-1>', game.mouse_clicked)
    canvas.update()

    width, height = canvas.winfo_width(), canvas.winfo_height()

    x_length = (width // game.N)
    y_length = (height // game.M)

    for i in range(game.N):
        for j in range(game.M):
            x = (i + 0.5) * x_length
            y = (j + 0.5) * y_length
            canvas.create_rectangle(x - x_length/2, y - y_length/2, x + x_length/2, y + y_length/2, fill=game.colours['off'])

def createControls(container):
    run_once = tk.Button(container, text='Run Once', command=game.run_gen)
    run_once.place(relx=0.1, rely=0.9)

    run_forever = tk.Button(container, text='Run Forever', command=game.run_forever)
    run_forever.place(relx=0.2, rely=0.9)

    change_time_interval = tk.Button(container, text='Change Speed', command=game.change_interval)
    change_time_interval.place(relx=0.3, rely=0.9)

    time_input = tk.Entry(container)
    time_input.insert(tk.END, game.time_interval)
    time_input.place(relx=0.4, rely=0.9)
    game.entry = time_input

if __name__ == '__main__':

    ########################
    # Initialize the window
    ########################
    root = tk.Tk()
    game.root = root

    root.title('Game of Life')

    # Set window to fullscreen mode, escape to quit
    root.attributes('-fullscreen', True)
    root.bind("<Escape>", lambda e: root.quit())

    # Make the canvas with the main grid and controls
    createGrid(root)
    createControls(root)

    # Create the window
    root.mainloop()
