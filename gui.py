import tkinter as tk
from tkinter import ttk


# Window Box -------------------------

root = tk.Tk()
root.title('Contact Book')

# Add Tabs -------------------------

tabControl = ttk.Notebook(root, width=520, height=520)
add_tab = tk.Frame(tabControl)
search_tab = tk.Frame(tabControl)
tabControl.add(add_tab, text='Add Contacts')
tabControl.add(search_tab, text='Search Contacts')
tabControl.grid(row=0, column=0)

# Background Images -------------------------

bg_img = tk.PhotoImage(file='contactbook.png')

background_label_add = tk.Label(add_tab, image=bg_img)
background_label_add.place(x=0, y=0, relwidth=1, relheight=1)

background_label_search = tk.Label(search_tab, image=bg_img)
background_label_search.place(x=0, y=0, relwidth=1, relheight=1)

# Buttons -------------------------

add_button = tk.Button(add_tab, text='Add Contact')
add_button.grid(row=5, column=0)

search_button = tk.Button(search_tab, text='Search Contact')
search_button.grid(row=6, column=0)

clear_button = tk.Button(text="Clear")
clear_button.grid(row=7, column=0)

exit_button = tk.Button(text="Exit")
exit_button.grid(row=8, column=0)

# Labels -------------------------

first_name_label = tk.Label(text='First Name:', bg='white')
first_name_label.grid(row=0, column=0)

last_name_label = tk.Label(text='Last Name:', bg='white')
last_name_label.grid(row=1, column=0)

cellphone_number_label = tk.Label(text='Cellphone number:', bg='white')
cellphone_number_label.grid(row=2, column=0)

email_label = tk.Label(text='Email:', bg='white')
email_label.grid(row=3, column=0)

home_number_label = tk.Label(text='Home number:',bg='white')
home_number_label.grid(row=4, column=0)

# Entry Boxes -------------------------

first_name_entry = tk.Entry()
first_name_entry.grid(row=0, column=2)

last_name_entry = tk.Entry()
last_name_entry.grid(row=1, column=2)

cellphone_number_entry = tk.Entry()
cellphone_number_entry.grid(row=2, column=2)

email_entry = tk.Entry()
email_entry.grid(row=3, column=2)

home_number_entry = tk.Entry()
home_number_entry.grid(row=4, column=2)

root.mainloop()

