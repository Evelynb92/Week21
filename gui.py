import tkinter as tk
from tkinter import ttk


# Window Box -------------------------

# root = tk.Tk()
# root.title('Contact Book')

# Add Tabs -------------------------

# tabControl = ttk.Notebook(root, width=520, height=520)
# add_tab = tk.Frame(tabControl)
# search_tab = tk.Frame(tabControl)
# tabControl.add(add_tab, text='Add Contacts')
# tabControl.add(search_tab, text='Search Contacts')
# tabControl.grid(row=0, column=0)
# #
# # Background Images -------------------------
#


class Gui:
  def __init__(self):
      self.root = tk.Tk()
      self.root.title('Contact Book')

      tabControl = ttk.Notebook(self.root, width=520, height=520)
      add_tab = tk.Frame(tabControl)
      search_tab = tk.Frame(tabControl)
      tabControl.add(add_tab, text='Add Contacts')
      tabControl.add(search_tab, text='Search Contacts')
      tabControl.grid(row=0, column=0)

      bg_img = tk.PhotoImage(file='contactbook.png')

      background_label_add = tk.Label(add_tab, image=bg_img)
      background_label_add.place(x=0, y=0, relwidth=1, relheight=1)

      background_label_search = tk.Label(search_tab, image=bg_img)
      background_label_search.place(x=0, y=0, relwidth=1, relheight=1)
    # Buttons -------------------------

      self.add_button = tk.Button(add_tab, text='Add Contact')
      self.add_button.grid(row=5, column=1)

      self.search_button = tk.Button(search_tab, text='Search Contact')
      self.search_button.grid(row=6, column=0)

      self.clear_button = tk.Button(text="Clear")
      self.clear_button.grid(row=7, column=0)

      self.exit_button = tk.Button(text="Exit")
      self.exit_button.grid(row=8, column=0)

    # Labels -------------------------

      self.first_name_label = tk.Label(add_tab, text='First Name:', bg='white')
      self.first_name_label.grid(row=0, column=0)

      self.last_name_label = tk.Label(add_tab, text='Last Name:', bg='white')
      self.last_name_label.grid(row=1, column=0)

      self.cellphone_number_label = tk.Label(add_tab, text='Cellphone number:', bg='white')
      self.cellphone_number_label.grid(row=2, column=0)

      self.email_label = tk.Label(add_tab,text='Email:', bg='white')
      self.email_label.grid(row=3, column=0)

      self.home_number_label = tk.Label(add_tab, text='Home number:', bg='white')
      self.home_number_label.grid(row=4, column=0)

    # Entry Boxes -------------------------

      self.first_name_entry = tk.Entry(add_tab)
      self.first_name_entry.grid(row=0, column=2)

      self.last_name_entry = tk.Entry(add_tab)
      self.last_name_entry.grid(row=1, column=2)

      self.cellphone_number_entry = tk.Entry(add_tab)
      self.cellphone_number_entry.grid(row=2, column=2)

      self.email_entry = tk.Entry(add_tab)
      self.email_entry.grid(row=3, column=2)

      self.home_number_entry = tk.Entry(add_tab)
      self.home_number_entry.grid(row=4, column=2)

# gui=Gui(root)
      self.root.mainloop()

