# -*- coding: utf-8 -*-
"""
Created on Sat Nov  8 19:38:26 2025

@author: Admin
"""
from tkinter import *
from tkinter import filedialog, messagebox

# Create main window
root = Tk()
root.title("Simple Text Editor")
root.geometry("600x400")

# Create Text Area
text_area = Text(root, wrap=WORD, font=("Arial", 12))
text_area.pack(expand=True, fill=BOTH)

# Define functions
def new_file():
    text_area.delete(1.0, END)

def open_file():
    file = filedialog.askopenfilename(defaultextension=".txt",
                                      filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file:
        text_area.delete(1.0, END)
        with open(file, "r") as f:
            text_area.insert(1.0, f.read())

def save_file():
    file = filedialog.asksaveasfilename(defaultextension=".txt",
                                        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file:
        with open(file, "w") as f:
            f.write(text_area.get(1.0, END))
        messagebox.showinfo("Success", "File saved successfully!")

def exit_app():
    root.destroy()

# Create Menu
menu_bar = Menu(root)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)
menu_bar.add_cascade(label="File", menu=file_menu)

root.config(menu=menu_bar)
root.mainloop()
