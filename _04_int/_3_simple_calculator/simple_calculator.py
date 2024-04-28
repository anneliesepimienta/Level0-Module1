"""
* Write a Python program that asks the user for two numbers.

* Then ask the user if the would like to add, subtract, multiply, or divide.

* Use if-else statements to provide the desired math operation on the numbers
  and display the result.
"""
from tkinter import messagebox, simpledialog, Tk
window = Tk()
window.withdraw()
number1 = simpledialog.askstring(title = "", prompt = "pick a number")
number2 = simpledialog.askstring(title = "", prompt = "pick another number")
question = simpledialog.askstring(title = "", prompt = "would you like to add, subtract, multiply, or divide?")
if question == "add":
    sum = int(number1) + int(number2)
    messagebox.showinfo(title = "the sum of those two numbers is...", message = str(sum))
if question == "subtract":
    subtract = int(number1) - int(number2)
    messagebox.showinfo(title = "the answer of those two numbers is...", message = str(subtract))
if question == "divide":
    divide = int(number1) / int(number2)
    messagebox.showinfo(title = "the answer of those two numbers is...", message = str(divide))
if question == "multiply":
    multiply = int(number1) * int(number2)
    messagebox.showinfo(title = "the answer of those two numbers is...", message =  str(multiply))

