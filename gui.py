import tkinter as tk
from tkinter import ttk
from add import save_contact
from contact import Contacts
from search import contact_searched

# Window Box -------------------------

# root = tk.Tk()
# root.title('Contact Book')

# Contact List -------------------------

contact_list = ['First Name:', 'Last Name: ', 'Cellphone number: ', 'E-mail: ', 'Home number: ']
counter = 0


# # Add Tabs -------------------------
# 
# tabControl = ttk.Notebook(root, width=520, height=520)
# self.add_tab = tk.Frame(tabControl)
# self.search_tab = tk.Frame(tabControl)
# tabControl.add(self.add_tab, text='Add Contacts')
# tabControl.add(self.search_tab, text='Search Contacts')
# tabControl.grid(row=0, column=0)
# 
# # Background Images -------------------------
# 
# bg_img = tk.PhotoImage(file='contactbook.png')
# 
# background_label_add = tk.Label(self.add_tab, image=bg_img)
# background_label_add.place(x=0, y=0, relwidth=1, relheight=1)
# 
# background_label_search = tk.Label(self.search_tab, image=bg_img)
# background_label_search.place(x=0, y=0, relwidth=1, relheight=1)


class Gui:
    def __init__(self):

        self.root = tk.Tk()
        self.root.title('Contact Book')

        # Add Tabs -------------------------

        self.tabControl = ttk.Notebook(self.root, width=520, height=520)
        self.add_tab = tk.Frame(self.tabControl)
        self.search_tab = tk.Frame(self.tabControl)
        self.tabControl.add(self.add_tab, text='Add Contacts')
        self.tabControl.add(self.search_tab, text='Search Contacts')
        self.tabControl.grid(row=0, column=0)

        # Background Images -------------------------

        bg_img = tk.PhotoImage(file='contactbook.png')

        background_label_add = tk.Label(self.add_tab, image=bg_img)
        background_label_add.place(x=0, y=0, relwidth=1, relheight=1)

        background_label_search = tk.Label(self.search_tab, image=bg_img)
        background_label_search.place(x=0, y=0, relwidth=1, relheight=1)

        # Add Buttons -------------------------

        self.add_button = tk.Button(self.add_tab, text='Add Contact', command=self.user_input)
        self.add_button.grid(row=7, column=7)

        self.clear_button = tk.Button(self.add_tab, text="Clear")
        self.clear_button.grid(row=10, column=10)

        self.exit_button = tk.Button(self.add_tab, text="Exit")
        self.exit_button.grid(row=11, column=10)

        # Search Buttons -------------------------

        self.search_button = tk.Button(self.search_tab, text='Search Contact', command=self.run_search)
        self.search_button.grid(row=7, column=2)

        self.clear_button = tk.Button(self.search_tab, text="Clear")
        self.clear_button.grid(row=10, column=2)

        self.exit_button = tk.Button(self.search_tab, text="Exit")
        self.exit_button.grid(row=11, column=2)

        #  Add Labels -------------------------

        self.first_name_label = tk.Label(self.add_tab, text='First Name:', bg='white')
        self.first_name_label.grid(row=2, column=5)

        self.last_name_label = tk.Label(self.add_tab, text='Last Name:', bg='white')
        self.last_name_label.grid(row=3, column=5)

        self.cellphone_number_label = tk.Label(self.add_tab, text='Cellphone number:', bg='white')
        self.cellphone_number_label.grid(row=4, column=5)

        self.email_label = tk.Label(self.add_tab, text='Email:', bg='white')
        self.email_label.grid(row=5, column=5)

        self.home_number_label = tk.Label(self.add_tab, text='Home number:', bg='white')
        self.home_number_label.grid(row=6, column=5)

        # Search Labels -------------------------

        self.first_name_search_label = tk.Label(self.search_tab, text='First Name:', bg='white')
        self.first_name_search_label.grid(row=0, column=0)

        self.last_name_search_label = tk.Label(self.search_tab, text='Last Name:', bg='white')
        self.last_name_search_label.grid(row=1, column=0)

        self.cellphone_number_search_label = tk.Label(self.search_tab, text='Cellphone number:', bg='white')
        self.cellphone_number_search_label.grid(row=2, column=0)

        self.email_search_label = tk.Label(self.search_tab, text='Email:', bg='white')
        self.email_search_label.grid(row=3, column=0)

        self.home_number_search_label = tk.Label(self.search_tab, text='Home number:', bg='white')
        self.home_number_search_label.grid(row=4, column=0)

        # Add Entry Boxes -------------------------

        self.first_name_entry = tk.Entry(self.add_tab)
        self.first_name_entry.grid(row=2, column=7)

        self.last_name_entry = tk.Entry(self.add_tab)
        self.last_name_entry.grid(row=3, column=7)

        self.cellphone_number_entry = tk.Entry(self.add_tab)
        self.cellphone_number_entry.grid(row=4, column=7)

        self.email_entry = tk.Entry(self.add_tab)
        self.email_entry.grid(row=5, column=7)

        self.home_number_entry = tk.Entry(self.add_tab)
        self.home_number_entry.grid(row=6, column=7)

        # Search Entry Boxes -------------------------

        self.first_name_search_entry = tk.Entry(self.search_tab)
        self.first_name_search_entry.grid(row=0, column=2)

        self.last_name_search_entry = tk.Entry(self.search_tab)
        self.last_name_search_entry.grid(row=1, column=2)

        self.cellphone_number_search_entry = tk.Entry(self.search_tab)
        self.cellphone_number_search_entry.grid(row=2, column=2)

        self.email_search_entry = tk.Entry(self.search_tab)
        self.email_search_entry.grid(row=3, column=2)

        self.home_number_search_entry = tk.Entry(self.search_tab)
        self.home_number_search_entry.grid(row=4, column=2)

        self.root.mainloop()

    # Capturing User Input -------------------------

    def user_input(self):

        current_contacts = Contacts(self.first_name_entry.get(), self.last_name_entry.get(),
                                    self.cellphone_number_entry.get(), self.email_entry.get(),
                                    self.home_number_entry.get())
        save_contact(current_contacts)

    # Searching User Input -------------------------
    def run_search(self):
        search_success = contact_searched(self.first_name_search_entry.get())

        if search_success.first_name != 'NOT FOUND':
            # self.last_name_search_entry.configure = tk.Entry(self.search_tab, text=search_success.last_name)
            # self.cellphone_number_search_entry.configure = tk.Entry(self.search_tab, text=search_success.cellphone_number)
            # self.email_search_entry.configure = tk.Entry(self.search_tab, text=search_success.email)
            # self.home_number_search_entry.configure = tk.Entry(self.search_tab, text = search_success.home_number)
            self.last_name_search_entry.insert(0, search_success.last_name)
        else:
            # self.last_name_search_entry.configure = tk.Entry(text='NOT FOUND')
            # self.cellphone_number_search_entry.configure = tk.Entry(self.search_tab, text='NOT FOUND')
            # self.email_search_entry.configure = tk.Entry(self.search_tab, text='NOT FOUND')
            # self.home_number_search_entry.configure = tk.Entry(self.search_tab, text='NOT FOUND')
            self.last_name_search_entry.insert(0, search_success.last_name)

# Gui = Gui(root)
