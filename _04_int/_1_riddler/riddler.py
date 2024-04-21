"""
* Write a python program that asks the user a minimum of 3 riddles.
simpledialog.askstring(title = "", prompt = "How do you make a poisonous snake cry?")
* You can look at riddles.com if you don't already know any riddles.

* Collect the response of each riddle from the user and compare their
  answers to the correct answer. 

* Use a variable to keep track of the correctly answered riddles

* After all the riddles have been asked, tell the user how many they got
  correct
"""

from tkinter import messagebox, simpledialog, Tk
window = Tk()
window.withdraw()
riddle = simpledialog.askstring(title = "", prompt = "How do you make a poisonous snake cry?")
answer = "take its rattle"
score = 0
if riddle == answer:
    messagebox.showinfo(title = "", message = "you are correct!")
    score = score + 1
else:
    messagebox.showinfo(title = "", message = "you are incorrect. answer is; take its rattle.")

riddle2 = simpledialog.askstring(title = "", prompt = "what can you hold in your left hand but not in your left?")
answer = "your left hand"
if riddle2 == answer:
    messagebox.showinfo(title = "", message = "you are correct!")
    score = score + 1
else:
    messagebox.showinfo(title = "", message = "you are incorrect. answer is; your left hand.")
riddle3 = simpledialog.askstring(title = "", prompt = "david's dad has three sons; snap, crackle, and _________?")
answer = "David"
if riddle3 == answer:
    messagebox.showinfo(title = "", message = "you are correct!")
    score = score + 1
else:
    messagebox.showinfo(title = "", message = "you are incorrect.answer; David.")

