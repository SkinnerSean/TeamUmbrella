import users
import tkinter as tk
from tkinter.ttk import *
from tkinter.filedialog import askopenfilename #used for uploading file

file_path = " "

# MENU1 IS THE MAIN MENU
class Menu1:
    def __init__(self, master):
        # WINDOW PROPERTIES
        self.master = master
        self.master.title("TEAM UMBRELLA")
        self.master.geometry('400x250')
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
            padx = 50,
            pady = 4,
            fg = "black",
            command = self.view_window
        )
        self.button_new = tk.Button(
            self.frame,
            text = "NEW",
            padx = 50,
            pady = 4,
            command = self.new_window
        )

        # DISPLAY
        self.title.grid(row = 0, column = 0, padx = 10, pady = 10)
        self.button_view.grid(row = 1, column = 0, padx = 4, pady = 4)
        self.button_new.grid(row = 2, column = 0, padx = 4, pady = 4)
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

        # INPUT PROMPTS
        self.user_prompt = tk.Entry(self.frame)
        self.profile_name_prompt = tk.Entry(self.frame)
        self.location_prompt = tk.Entry(self.frame)

        # LABELS
        self.l1 = tk.Label(self.frame, text = "Username:")
        self.l2 = tk.Label(self.frame, text = "Engine Profile Name:")
        self.l3 = tk.Label(self.frame, text = "Location:")
        self.l4 = tk.Label(self.frame, text = "uploaded file", foreground = "green")


        # BUTTONS
        self.file_upload = tk.Button(
            self.frame,
            padx = 20,
            text = 'Upload XLSX File',
            command = lambda:self.open_file()
        )
        self.register_profile= tk.Button( 
            self.frame,
            padx = 10,
            text = 'Register Profile',
            command = self.quit
        )

        # DISPLAY
        self.l1.grid(row = 0, column = 0, sticky = 'w')
        self.l2.grid(row = 1, column = 0, sticky = 'w')
        self.l3.grid(row = 2, column = 0, sticky = 'w')
        self.user_prompt.grid(row = 0, column = 1, sticky = 'w', pady = 8)
        self.profile_name_prompt.grid(row = 1, column = 1, sticky = 'w', pady = 4)
        self.location_prompt.grid(row = 2, column = 1, sticky = 'w', pady = 4)
        self.file_upload.grid(row = 3, column = 0, pady = 4)
        self.register_profile.grid(row = 4, column = 0, columnspan = 2, pady = 4)


        self.frame.pack()

    # FOR UPLOADING FILE
    def open_file(self):
        file_name = askopenfilename()   # = askopenfile(mode = 'r', filetypes = [('xlsx Files', '*.xlsx')])
        if file_name is not None:
            global file_path 
            file_path = file_name # this is where we will call menu to process data and store in db
            self.l4.grid(row = 3, column = 1, sticky = 'w')
                    
    # FOR CLOSING WINDOW AND SENDING DATA TO USER CLASS
    def quit(self):
        print(self.user_prompt.get())
        print(self.profile_name_prompt.get())
        print(self.location_prompt.get())
        print(file_path)
        # new_profile(self.user_prompt.get(), self.profile_name_prompt.get(), self.location_prompt.get(), global file_path)
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