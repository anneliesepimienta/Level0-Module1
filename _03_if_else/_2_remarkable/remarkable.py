from tkinter import messagebox, simpledialog, Tk
window = Tk()
window.withdraw()


warrior1 = "flyingspots"
warrior2 = "butterflyperch"
warrior3 = "stormhaze"
warrior4 = "northgaze"
warrior5 = "sunblaze"
warrior6 = "glimmereyes"
warrior7 = "sweetheart"

warrior = simpledialog.askstring(title = "cat", prompt = "what's your name?")
if warrior == warrior1:
    messagebox.showinfo(title = "", message = "you are great at climbing trees!")
elif warrior == warrior2:
    messagebox.showinfo(title = "", message = "you have pretty fur!")
elif warrior == warrior3:
    messagebox.showinfo(title = "", message = "you are a great hunter!")
elif warrior == warrior4:
    messagebox.showinfo(title = "", message = "you are a great fighter in battle!")
elif warrior == warrior5:
    messagebox.showinfo(title = "", message = "you are a great friend!")
elif warrior == warrior6:
    messagebox.showinfo(title = "", message = "your have beautiful eyes!")
elif warrior == warrior7:
    messagebox.showinfo(title = "", message = "you are great with herbs!")
else:
    messagebox.showinfo(title = "", message = "x_x")
