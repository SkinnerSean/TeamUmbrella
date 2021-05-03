from user import User
import tkinter as tk
from tkinter.ttk import *
from tkinter.filedialog import askopenfilename #used for uploading file

file_path = " "

# MENU1 IS THE MAIN MENU
class Menu1:
    def __init__(self, master):
        # WINDOW PROPERTIES
        self.users = [] # only works during run time cannot load profiles in yet
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
        self.app = Menu2(self.newWindow,self.users)

    # FOR OPENING MENU3
    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Menu3(self.newWindow,self.users)

# MENU2 IS TO VIEW PROFILES
class Menu2:
    def __init__ (self, master,profiles):
        self.users = profiles
        # WINDOW PROPERTIES
        self.master = master
        self.master.title("HYDROPLANES")
        self.master.geometry('600x450')
        self.frame = tk.Frame(self.master)

        # INPUT PROMPTS
        self.user_prompt = tk.Entry(self.frame)

        # LABELS
        self.l1 = tk.Label(self.frame, text = "View Hydroplane Profiles for User:")

        # BUTTONS
        self.user_search = tk.Button(
            self.frame,
            padx = 5,
            text = 'Search',
            command = self.validateUser
        )

        # DISPLAY
        self.l1.grid(row = 0, column = 0, sticky = 'w')
        self.user_prompt.grid(row = 0, column = 1, sticky = 'w', pady = 8)
        self.user_search.grid(row = 0, column = 2)
        self.frame.pack()

    # FOR VALIDATING USER INPUT
    def validateUser(self):
        u = User(self.user_prompt.get())
        
        print("Validating user input....")
        print_profiles = ' '
        for name,stats in u.get_profiles_iterable():
<<<<<<< HEAD
            print_profiles += f"Name: {name} - Location: {stats['location']}\nStats - {stats['stats']}\n\n"

        query_label = Label(self.frame, text = print_profiles)
        query_label.grid(row = 1, column = 0, columnspan = 2)
=======
>>>>>>> 2444975a1a058fbba8eb88ce9729b0bf7a7f2770
        # if there is a user with name matching self.user_prompt.get()
            # user found, continue with display
        # else
            # user not found, try again



# MENU3 IS TO UPLOAD NEW PROFILE
class Menu3:
    def __init__ (self, master,profiles):
        self.users = profiles
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
        self.l1 = tk.Label(self.frame, text = "Username")
        self.l2 = tk.Label(self.frame, text = "Engine Profile Name")
        self.l3 = tk.Label(self.frame, text = "Location")

        # BUTTONS
        self.file_upload = tk.Button(
            self.frame,
            padx = 20,
            text = 'Upload XLSX File',
            command = lambda:self.openFile()
        )
        self.register_profile= tk.Button( 
            self.frame,
            padx = 10,
            text = 'Register Profile',
            command = self.update_DB
        )
        self.exit_menu = tk.Button(
            self.frame,
            padx = 10,
            text = "Done",
            command = self.quit
        )

        # DISPLAY
        self.l1.grid(row = 0, column = 0, sticky = 'w', padx = 5)
        self.l2.grid(row = 1, column = 0, sticky = 'w', padx = 5)
        self.l3.grid(row = 2, column = 0, sticky = 'w', padx = 5)
        self.user_prompt.grid(row = 0, column = 1, sticky = 'w', pady = 8)
        self.profile_name_prompt.grid(row = 1, column = 1, sticky = 'w', pady = 4)
        self.location_prompt.grid(row = 2, column = 1, sticky = 'w', pady = 4)
        self.file_upload.grid(row = 3, column = 0, columnspan = 2, pady = 4)
        self.register_profile.grid(row = 4, column = 0, columnspan = 2, pady = 4)
        self.exit_menu.grid(row = 5, column = 0, columnspan = 2, pady = 10)
        self.frame.pack()

    # FOR UPLOADING FILE
    def openFile(self):
        file_name = askopenfilename()   # = askopenfile(mode = 'r', filetypes = [('xlsx Files', '*.xlsx')])
        if file_name is not None: # this if conditional is always true !!!!
            global file_path 
            file_path = file_name 

    # FOR APPENDING NEW DATA INTO DATABASE
    def update_DB(self):
        global file_path
        u = User(self.user_prompt.get())
        u.new_profile(self.profile_name_prompt.get(), self.location_prompt.get(), file_path)
        self.user_prompt.delete(0, 'end')
        self.profile_name_prompt.delete(0, 'end')
        self.location_prompt.delete(0, 'end')

    # FOR CLOSING WINDOW AND SENDING DATA TO USER CLASS
    def quit(self):
        self.master.destroy()
        



# MAIN PROGRAM LOOP
def main():
    root = tk.Tk()
    app = Menu1(root)
    root.mainloop()

if __name__ == '__main__':
    main()
