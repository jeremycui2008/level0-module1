import turtle
from tkinter import messagebox, simpledialog, Tk
import math

# Goal: Write a Python program that asks the user for the radius 
#       of a circle and displays the area of that circle.
#       The formula for the area of a circle is πr^2.
#       See example image in package to check your output.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Ask the user for the radius in pixels and store it in a variable
    size= simpledialog.askinteger(title='radius', prompt='whats the radius of your circle in pixels?')
    
    # Make a new turtle
    bill= turtle.Turtle()
    # Have your turtle draw a circle with the correct radius
    bill.circle(size)
    bill.penup()
    bill.goto(40, 70)
    # Call the turtle .penup() method

    # Move your turtle to a new x,y position using .goto()

    # Calculate the area of your circle and store it in a variable
    # Hint, you can use math.pi
    area=math.pi
    
    # Write the area of your circle using the turtle .write() method

    bill.write(arg="area = " + str(area), move=True, align='left', font=('Arial',8,'normal'))

    # Hide your turtle
    bill.hideturtle()
    # Call turtle.done()
    window.mainloop()
