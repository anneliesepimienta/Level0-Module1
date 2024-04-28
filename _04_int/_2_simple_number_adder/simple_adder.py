"""
* Write a Python program that asks the user for two numbers.

* Display the sum of the two numbers to the user
"""
from tkinter import messagebox, simpledialog, Tk
window = Tk()
window.withdraw()
score = 0
number1 = simpledialog.askstring(title = "", prompt = "pick a number")
number2 = simpledialog.askstring(title = "", prompt = "pick another number")
sum = int(number1) + int(number2)
messagebox.showinfo(title = "the sum of those two numbers is...", message = str(sum))
