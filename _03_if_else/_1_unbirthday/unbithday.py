import turtle
from tkinter import messagebox, simpledialog, Tk
window = Tk()
window.withdraw()
birthday =simpledialog.askstring(title = "birthday", prompt ="when is your birthday month and day?")
birthday = int(birthday)
if birthday == 407:
    messagebox.showinfo(title = "birthday", message ="i wish you a happy birthday!")
else:
    messagebox.showinfo(title = "birthday", message ="merry UNbirthday!")

