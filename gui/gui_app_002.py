from tkinter import *
from tkinter import messagebox
top = Tk()

def drawLED(x: int, y: int, C: Canvas):
    coord = x - 10, y - 10, x + 10, y + 10
    
    arc_R = C.create_arc(coord, start=0, extent=119, fill="#ff0000")
    arc_G = C.create_arc(coord, start=120, extent=119, fill="#00ff00")
    arc_B = C.create_arc(coord, start=240, extent=119, fill="#0000ff")
    C.pack()




C = Canvas(top, bg="white", height=250, width=300)
drawLED(20, 20, C)
drawLED(60, 20, C)
drawLED(100, 20, C)
drawLED(140, 20, C)

top.mainloop()