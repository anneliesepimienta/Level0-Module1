# Write a Python program that asks the user for the radius of a circle.
# Next, ask the user if they would like to calculate the area or circumference of a circle.
# If they choose area, display the area of the circle using the radius.
# Otherwise, display the circumference of the circle using the radius.

#Area = πr^2
#Circumference = 2πr

from math import pi
from tkinter import messagebox, simpledialog, Tk
window = Tk()
window.withdraw()
value = ""
radius = simpledialog.askinteger(title = "", prompt = "enter a radius")
operation = simpledialog.askstring(title = "", prompt = "would you like to calculate the area or circumference?")
if operation == "area":
    value = "area=" +str(pi*radius**2)
else:
    value = "circumference=" +str(2*pi*radius)
messagebox.showinfo(title = "", message = value)
