import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import PhotoImage

# Window Box -------------------------

root = tk.Tk()
root.title('Contact Book')

# Add Tab -------------------------

tabControl = ttk.Notebook(root, width=570, height=350)
add_tab = Frame(tabControl)
search_tab = Frame(tabControl)
tabControl.add(add_tab, text='Add Contacts')
tabControl.add(search_tab, text='Search Contacts')
tabControl.grid(row=0, column=0)

# Background Images -------------------------

bg_img = PhotoImage(file='contactbook.png')
background_label_add = Label(add_tab, image=bg_img)
background_label_search = Label(search_tab, image=bg_img)

# Buttons -------------------------

add_button = Button(add_tab, text='Add Contact')

search_button = Button(search_tab, text='Search Contact')