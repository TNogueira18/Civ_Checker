import tkinter
from tkinter import *
from tkinter import ttk, filedialog
import sqlite3

# Build Functions

def Enter_Widget(event):
    event.widget.config(background = "#75BFFD")

def Leave_Widget(event):
    event.widget.config(background = "#0097FF")

def Query():
        # Connect to the database (creates a new file if it doesn't exist)
    conn = sqlite3.connect("Database.db")
    Database_executer = conn.cursor()

    Database_executer.execute("Select oid, * from Final")
    Data = Database_executer.fetchall()

    conn.commit()
    conn.close()

    return Data

def Database():

    Data = []

    # Pull the data out of the database
    Data = Query()

    print(Data)

def Select_File():
    App.withdraw()
    File_Path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
    App.deiconify()
    return File_Path

def Checker():

    Data = Select_File()

    results = []
    results_stack = 0
    stacking_list = []
    k = 0

    while k < len(data["bonuses"][0]):
        if "and" in data01[data["bonuses"][0][k]][3]:
            slt = [data01[data["bonuses"][0][k]][3].split(" and ")]
            c = 0
            while c < len(slt[0]):
                stacking_list += [slt[0][c]]
                c += 1
        else:
            stacking_list += [data01[data["bonuses"][0][k]][3]]
        k += 1

    for i in data["bonuses"][0]:
        k = 0
        while True:
            if i+1 == data01[k][0]:
                results += [data01[k][2]]
            k += 1
            if k == len(data01):
                break

    results_stack = 0
    if "ARCHER BONUS" in stacking_list and stacking_list.count("ARCHER BONUS") > 0:
        results_stack += (stacking_list.count("ARCHER BONUS"))-1
    if "SIEGE BONUS" in stacking_list and stacking_list.count("SIEGE BONUS") > 0:
        results_stack += (stacking_list.count("SIEGE BONUS"))-1
    if "BUILDING BONUS" in stacking_list and stacking_list.count("BUILDING BONUS") > 0:
        results_stack += (stacking_list.count("BUILDING BONUS"))-1
    if "CAV BONUS" in stacking_list and stacking_list.count("CAV BONUS") > 0:
        results_stack += (stacking_list.count("CAV BONUS"))-1
    if "INFANTRY BONUS" in stacking_list and stacking_list.count("INFANTRY BONUS") > 0:
        results_stack += (stacking_list.count("INFANTRY BONUS"))-1
    if "DISCOUNT BONUS" in stacking_list and stacking_list.count("DISCOUNT BONUS") > 0:
        results_stack += (stacking_list.count("DISCOUNT BONUS"))-1
    if "ECO BONUS" in stacking_list and stacking_list.count("ECO BONUS") > 0:
        results_stack += (stacking_list.count("ECO BONUS"))-1
    if "MISC BONUS" in stacking_list and stacking_list.count("MISC BONUS") > 0:
        results_stack += (stacking_list.count("MISC BONUS"))-1
    if "NAVAL BONUS" in stacking_list and stacking_list.count("NAVAL BONUS") > 0:
        results_stack += (stacking_list.count("NAVAL BONUS"))-1
    if "MONK BONUS" in stacking_list and stacking_list.count("MONK BONUS") > 0:
        results_stack += (stacking_list.count("MONK BONUS"))-1
    if "RESOURCE BONUS" in stacking_list and stacking_list.count("RESOURCE BONUS") > 0:
        results_stack += (stacking_list.count("RESOURCE BONUS"))-1

    # check the bonus type, 3rd place

    if sum(results) + results_stack > 8:
        text01 = "Unaproved with " + str(sum(results) + results_stack - 8) + " points over"
    elif sum(results) + results_stack == 8:
        text01 = "Aproved"
    else:
        text01 = str(8 - (sum(results) + results_stack)) + " points left"

    text02 = str(data["alias"] + "\n\n")
    for i in data["bonuses"][0]:
        text02 += str(data01[i][3] + ", ") + str(data01[i][2]) + ", " + str(data01[i][1] + "\n")

    text02 += "\nStacking Penalty: " + str(results_stack)

    if "UNAVALIBLE" in stacking_list:
        text01 = "This civ has got the one civ bonus which is ilegal, Long Swordsman, Two-Handed Swordsman upgrades available one age earlier"

    lb = [69, 70, 71, 72, 73]
    for i in data["bonuses"][4]:
        if i in lb:
            text01 = "This civ has one of the 5 unavalible Team Bonus"
            break


    print(text01)
    print(text02)

def Check_Civ():
    
    Select_File()
    

def Home_Page():
    
    # Config the Buttons
    Button01.config(text = "Database", command = Database)
    Button02.config(text = "Check Civ", command = Check_Civ)

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

# Create Treeview 
tree = ttk.Treeview(App)

# Add columns
tree["columns"] = ("Column01", "Column02", "Column03", "Column04")
tree.column("#0", width=0, stretch = 0)
tree.column("Column01", width=100)
tree.column("Column02", width=100)
tree.column("Column03", width=100)
tree.column("Column04", width=100)

# Add headings
tree.heading("#0", text="")
tree.heading("Column01", text="Bonus ID")
tree.heading("Column02", text="Bonus Type")
tree.heading("Column03", text="Bonus Cost")
tree.heading("Column04", text="Bonus Description")

tree.tag_configure("oddrow", background="#D9D9D9", foreground = "#0097FF")
tree.tag_configure("evenrow", background="#0097FF", foreground = "#D9D9D9")

"""
global count
count = 0

for record in data:
    if count % 2 == 0:
        my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2]), tags=('evenrow',))
    else:
        my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2]), tags=('oddrow',))
    count += 1
"""
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