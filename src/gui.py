#import menu
import tkinter as tk

window_master = tk.Tk() #makes new window
window_master.geomtry = ('100x100')
window_master.title("Team Umbrella")

#this will be where menu class function are called to display information
def openNewWindow():
    newWindow = tk.Toplevel(window_master)
    newWindow.title("VIEWING ENGINE PROFILES")
    newWindow.geometry('200x200')
    tk.Label(newWindow, text = "this is info").pack()


#labels and buttons for main menu
greeting = tk.Label(
    window_master,
    text = "HYDROPLANE RACING APPLICATION",
    fg = "white",
    bg = "grey", 
    width = 50   
)
b_view = tk.Button(
    window_master,
    text = "VIEW",
    width = 25,
    height = 5,
    bg = "grey",
    fg = "black",
    command = openNewWindow #function to call on menu
)
b_new = tk.Button(
    window_master,
    text = "NEW",
    width = 25,
    height = 5,
    bg = "grey",
    fg = "black"
    #command = new_profile
)


greeting.pack()
b_new.pack()
b_view.pack()


window_master.mainloop()
