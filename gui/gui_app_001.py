import tkinter as tk

window = tk.Tk()
window.title("My First GUI App")
window.minsize(800, 600)
window.geometry("800x600+50+50")

greeting = tk.Label(window, text="Hello, Tkinter", font=("Arial", 24))
greeting.pack()

window.mainloop()