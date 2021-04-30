#import menu
import tkinter as tk
from tkinter.ttk import *
from tkinter.filedialog import askopenfilename #used for uploading file

# MENU1 IS THE MAIN MENU
class Menu1:
    def __init__(self, master):
        # WINDOW PROPERTIES
        self.master = master
        self.master.title("TEAM UMBRELLA")
        self.master.geometry('350x200')
        self.frame = tk.Frame(self.master)

        # LABEL
        self.title = tk.Label(
            self.frame,
            text = "HYDROPLANE RACING APPLICATION"
        )

        # BUTTONS
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

        # DISPLAY
        self.title.pack()
        self.button_view.pack()
        self.button_new.pack()
        self.frame.pack()

    # FOR OPENING MENU2
    def view_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Menu2(self.newWindow)

    # FOR OPENING MENU3
    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Menu3(self.newWindow)

# MENU2 IS TO VIEW PROFILES
class Menu2:
    def __init__ (self, master):
        # WINDOW PROPERTIES
        self.master = master
        self.master.title("HYDROPLANES")
        self.master.geometry('350x200')
        self.frame = tk.Frame(self.master)

        # DISPLAY
        self.prompt = tk.Label(self.frame, text = "GUI->MENU->USERDATA")
        self.prompt.pack()
        self.frame.pack()

# MENU3 IS TO UPLOAD NEW PROFILE
class Menu3:
    def __init__ (self, master):
        # WINDOW PROPERTIES
        self.master = master
        self.master.title("ADD HYROPLANE")
        self.master.geometry('350x200')
        self.frame = tk.Frame(self.master)

        # BUTTONS
        self.button_upload = tk.Button(
            self.frame,
            text = 'Upload XLSX File',
            command = lambda:self.open_file()
        )
        self.button_done= tk.Button(
            self.frame,
            text = 'DONE',
            command = self.quit
        )

        # DISPLAY
        self.prompt = tk.Label(self.frame, text = "COLLECT CSV -> MENU -> USER -> PROCESS CSV INTO PROFILE")
        self.prompt.pack()
        self.button_upload.pack()
        self.button_done.pack()
        self.frame.pack()

    # FOR UPLOADING FILE
    def open_file(self):
        file_name = askopenfilename()   # = askopenfile(mode = 'r', filetypes = [('xlsx Files', '*.xlsx')])
        if file_name is not None:
            #content = file_name.read() # this is where we will call menu to process data and store in db
            print(file_name)
        
    # FOR CLOSING WINDOW
    def quit(self):
        self.master.destroy()

# MAIN PROGRAM LOOP
def main():
    root = tk.Tk()
    app = Menu1(root)
    root.mainloop()

if __name__ == '__main__':
    main()




# #create a database or connect to one
# conn = sqlite3.connect('user_hydroplanes.db')

# #creating cursor instance
# c = conn.cursor()

# #creating cols for the database table
# c.execute("""CREATE TABLE addresses (
#     profile_name text,
#     location text

    
#     )""")




# #commit changes made
# conn.commit()

# #close connection
# conn.close()

# #text, integers, real, null, blob(img,vid)