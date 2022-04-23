from tkinter import simpledialog, messagebox, Tk
import tkinter as tk
if __name__ == '__main__':

    window_width = 600
    window_height = 600

    root = tk.Tk()

    canvas = tk.Canvas(root, width=window_width, height=window_height, bg="#DDDDDD")
    canvas.grid()

# 1. Ask the user what color tomato they would like and save their response
#    You can give them up to three choices
    tomato_color= simpledialog.askstring(title='what color you want tomato?', prompt='what color would you like your tomato to be?')

# 2. Use if-else statements to draw the tomato in the color that they chose
#    You can modify the code below or draw your own tomato
if tomato_color== 'red':
    canvas.create_oval(75, 200, 400, 450, fill="red", outline="")
    canvas.create_oval(200, 200, 525, 450, fill="red", outline="")
    canvas.create_rectangle(275, 100, 325, 230, fill="blue", outline="")
if tomato_color== 'blue':
    canvas.create_oval(75, 200, 400, 450, fill="blue", outline="")
    canvas.create_oval(200, 200, 525, 450, fill="blue", outline="")
    canvas.create_rectangle(275, 100, 325, 230, fill="orange", outline="")
if tomato_color== 'purple':
    canvas.create_oval(75, 200, 400, 450, fill="purple", outline="")
    canvas.create_oval(200, 200, 525, 450, fill="purple", outline="")
    canvas.create_rectangle(275, 100, 325, 230, fill="yellow", outline="")

root.mainloop()
