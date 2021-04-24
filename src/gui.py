#import menu
import tkinter as tk

class Menu1:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.title = tk.Label(
            self.frame,
            text = "HYDROPLANE RACING APPLICATION"
        )
        self.button_view = tk.Button(
            self.frame,
            text = "VIEW",
            width = 25,
            height = 5,
            bg = "grey",
            fg = "black"
        )
        self.button_new = tk.Button(
            self.frame,
            text = "NEW",
            width = 25,
            height = 5,
            bg = "grey",
            fg = "black"
        )
        self.title.pack()
        self.button_view.pack()
        self.button_new.pack()
        self.frame.pack()


#class viewHydros
#class newHydro

def main():
    root = tk.Tk()
    app = Menu1(root)
    root.mainloop()

if __name__ == '__main__':
    main()
