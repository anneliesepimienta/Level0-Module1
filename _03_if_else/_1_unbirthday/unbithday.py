import turtle
from tkinter import messagebox, simpledialog, Tk
window = Tk()
window.withdraw()
birthday =simpledialog.askstring(title = "birthday", prompt ="when is your birthday month and day?")
if birthday == 407:
    simpledialog.askstring(title = "birthday", prompt ="i wish you a happy birthday!")
else:
    simpledialog.askstring(title = "birthday", prompt ="merry UNbirthday!")
