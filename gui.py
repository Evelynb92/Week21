import tkinter as tk
import ttk

# Window Box -------------------------

root = tk.Tk()
root.title('Contact Book')

# Add Tab -------------------------

tabControl = ttk.Notebook(root, width=570, height=350)
add_tab = tk.Frame(tabControl)
search_tab = tk.Frame(tabControl)
tabControl.add(add_tab, text='Add Contacts')
tabControl.add(search_tab, text='Search Contacts')
tabControl.grid(row=0, column=0)

# Background Images -------------------------

bg_img = tk.PhotoImage(file='contactbook.png')
background_label_add = tk.Label(add_tab, image=bg_img)
background_label_search = tk.Label(search_tab, image=bg_img)

# Buttons -------------------------

add_button = tk.Button(add_tab, text='Add Contact')

search_button = tk.Button(search_tab, text='Search Contact')