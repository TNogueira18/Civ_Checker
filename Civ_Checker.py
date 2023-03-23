import tkinter
from tkinter import *
import sqlite3

# Build Functions

def Enter_Widget(event):
    event.widget.config(background = "#75BFFD")

def Leave_Widget(event):
    event.widget.config(background = "#0097FF")

def Database():
    return

def Check():
    return

def Home_Page():
    
    # Config the Buttons
    Button01.config(text = "Database", command = Database)
    Button02.config(text = "Check Civ", command = Check)

    # Place Buttons
    Button01.place(relheight = 0.1, relwidth = 0.2, relx = 0.4, rely = 0.7)
    Button02.place(relheight = 0.1, relwidth = 0.2, relx = 0.4, rely = 0.85)

    # Place Label
    Label01.place(relheight = 0.1, relwidth = 0.8, relx = 0.1, rely = 0.1)

# Build GUI

# Create App
App = Tk()

# Get screen width and height
screen_width = App.winfo_screenwidth()
screen_height = App.winfo_screenheight()

# Calculate window size and position
window_width = int(screen_width * 2/3)
window_height = int(screen_height * 2/3)
window_x = int((screen_width - window_width) / 2)
window_y = int((screen_height - window_height) / 2)

# Set window size and position
App.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

# Create Label
Label01 = Label(App, font = "Arial 50", justify = "center", foreground = "#0097FF", relief = "flat", text="Civ Checker")

# Create Buttons
Button01 = Button(App, background = "#0097FF", foreground = "#D9D9D9", activebackground = "#000CFF", activeforeground = "#D9D9D9", relief = "flat", font = "Arial 16")
Button02 = Button(App, background = "#0097FF", foreground = "#D9D9D9", activebackground = "#000CFF", activeforeground = "#D9D9D9", relief = "flat", font = "Arial 16")
Button03 = Button(App, background = "#0097FF", foreground = "#D9D9D9", activebackground = "#000CFF", activeforeground = "#D9D9D9", relief = "flat", font = "Arial 16")

# Place the binding in the Widgets
# Enter
Button01.bind("<Enter>", Enter_Widget)
Button02.bind("<Enter>", Enter_Widget)
Button03.bind("<Enter>", Enter_Widget)

# Leave
Button01.bind("<Leave>", Leave_Widget)
Button02.bind("<Leave>", Leave_Widget)
Button03.bind("<Leave>", Leave_Widget)


# Run Home Page
Home_Page()

# Make App run
App.mainloop()