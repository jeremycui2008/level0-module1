import math
from tkinter import simpledialog, messagebox, Tk
import tkinter as tk
if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    radius = simpledialog.askinteger(title='size', prompt='what is the radius of your circle?')
    #Write a Python program that asks the user for the radius of a circle.
    # Next, ask the user if they would like to calculate the area or circumference of a circle.
    yes=simpledialog.askstring(title='radius or circumference?', prompt='do you want the radius or circumference of your circle?')
    # If they choose area, display the area of the circle using the radius.
    if yes=='area':
        Area = math.pi*(radius**2)
        print(Area)
    if yes=='circumference':
        Circumference = 2*math.pi
        print(Circumference)
    # Otherwise, display the circumference of the circle using the radius.

    #
    #Circumference = 2πr
