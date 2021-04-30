#import menu
import tkinter as tk

class Menu1:
    def __init__(self, master):
        self.master = master
        self.master.title("TEAM UMBRELLA")
        self.master.geometry('350x200')
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
            fg = "black",
            command = self.view_window
        )
        self.button_new = tk.Button(
            self.frame,
            text = "NEW",
            width = 25,
            height = 5,
            bg = "grey",
            fg = "black",
            command = self.new_window
        )
        self.title.pack()
        self.button_view.pack()
        self.button_new.pack()
        self.frame.pack()

    def view_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Menu2(self.newWindow)

    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Menu3(self.newWindow)


class Menu2:
    def __init__ (self, master):
        self.master = master
        self.master.title("HYDROPLANES")
        self.master.geometry('350x200')
        self.frame = tk.Frame(self.master)
        self.prompt = tk.Label(self.frame, text = "GUI->MENU->USERDATA")
        self.prompt.pack()
        self.frame.pack()

class Menu3:
    def __init__ (self, master):
        self.master = master
        self.master.title("ADD HYROPLANE")
        self.master.geometry('350x200')
        self.frame = tk.Frame(self.master)
        self.prompt = tk.Label(self.frame, text = "COLLECT CSV -> MENU -> USER -> PROCESS CSV INTO PROFILE")
        self.prompt.pack()
        self.frame.pack()

def main():
    root = tk.Tk()
    app = Menu1(root)
    root.mainloop()

if __name__ == '__main__':
    main()
