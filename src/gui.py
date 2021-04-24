#import menu
import tkinter as tk

window = tk.Tk()
window.geomtry = ('100x100')
window.title("Team Umbrella")

greeting = tk.Label(
    text = "HYDROPLANE RACING APPLICATION",
    fg = "white",
    bg = "grey", 
    width = 50   
)

b_view = tk.Button(
    text = "VIEW",
    width = 25,
    height = 5,
    bg = "grey",
    fg = "black"
)


b_new = tk.Button(
    text = "NEW",
    width = 25,
    height = 5,
    bg = "grey",
    fg = "black"
)

greeting.pack()
b_new.pack()
b_view.pack()


window.mainloop()
