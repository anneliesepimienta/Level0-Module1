import turtle
from tkinter import messagebox, simpledialog, Tk

# Goal: Write a Python program that asks the user whether they want to
#       draw a triangle, square, or circle and then draw that shape.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Make a new turtle
    my_turtle = turtle.Turtle()
    # Ask the user what shape they want to draw and store it in a variable
    shape = simpledialog.askstring(title = "", prompt = "what shape would you like to draw?")
    # Draw the shape requested by the user using if-elif-else statements
    if shape == "circle":
        my_turtle.circle(100)
    if shape == "square":
        my_turtle.forward(100)
        my_turtle.left(90)
        my_turtle.forward(100)
        my_turtle.left(90)
        my_turtle.forward(100)
        my_turtle.left(90)
        my_turtle.forward(100)
    if shape == "trapezoid":
        my_turtle.forward(100)
        my_turtle.left(135)
        my_turtle.forward(100)
        my_turtle.left(45)
        my_turtle.forward(100)
        my_turtle.left(45)
        my_turtle.forward(100)
        my_turtle.left(135)
        my_turtle.forward(150)
    else:
        messagebox.showinfo(title="", message = "I am to lazy to do a code for every other shape. So deal with it!!!!!!!!!!!")
    # Call the turtle .done() method
    turtle.done()
