from tkinter import *
from tkinter import ttk, filedialog
import sqlite3
import json

# Build Functions

def Hide_Widgets():
    # Hide Widgets
    # Labels
    Label02.place_forget()

    # Butoons
    Button01.place_forget()
    Button02.place_forget()

    # Tree
    Tree_Frame.place_forget()
    Tree.delete(*Tree.get_children())

def Enter_Widget(event):
    event.widget.config(background = "#75BFFD")

def Leave_Widget(event):
    event.widget.config(background = "#0097FF")

def Query(Type):
    # Connect to the database (creates a new file if it doesn't exist)
    conn = sqlite3.connect("\Civ_Checker\Database.db")
    Database_executer = conn.cursor()

    if Type == "Normal":

        Database_executer.execute("SELECT oid, * FROM Final")

    else:

        Database_executer.execute("SELECT oid, * FROM Final ORDER BY {}".format(Type))

    # Pull the data
    Data = Database_executer.fetchall()

    conn.commit()
    conn.close()

    # Return the data to the code
    return Data

def Apply(POPUP, Value):
    # Clear Treeview
    Tree.delete(*Tree.get_children())

    # Destroy POPUP
    POPUP.destroy()

    # Query database
    Database(Value)

def Filter():

    # Create PopUp
    POPUP = Toplevel(App)

    # Define the sizes of the POPUP
    POPUP_width = int(screen_width * 1/3)
    POPUP_height = int(screen_height * 1/3)
    POPUP_x = int((screen_width - window_width))
    POPUP_y = int((screen_height - window_height))

    # Applies the sizes defined earlier
    POPUP.geometry(f"{POPUP_width}x{POPUP_height}+{POPUP_x}+{POPUP_y}")

    # Create POPUP Buttons
    Button_POPUP_01 = Button(POPUP, background = "#0097FF", foreground = "#D9D9D9", activebackground = "#000CFF", activeforeground = "#D9D9D9", relief = "flat", font = "Arial 14")
    Button_POPUP_02 = Button(POPUP, background = "#0097FF", foreground = "#D9D9D9", activebackground = "#000CFF", activeforeground = "#D9D9D9", relief = "flat", font = "Arial 14")
    Button_POPUP_03 = Button(POPUP, background = "#0097FF", foreground = "#D9D9D9", activebackground = "#000CFF", activeforeground = "#D9D9D9", relief = "flat", font = "Arial 14")
    Button_POPUP_04 = Button(POPUP, background = "#0097FF", foreground = "#D9D9D9", activebackground = "#000CFF", activeforeground = "#D9D9D9", relief = "flat", font = "Arial 14")


    # Config the Buttons
    Button_POPUP_01.config(text = "ID", command = lambda: Apply(POPUP, "oid"))
    Button_POPUP_02.config(text = "Type", command = lambda: Apply(POPUP, "Type"))
    Button_POPUP_03.config(text = "Cost", command = lambda: Apply(POPUP, "Points"))
    Button_POPUP_04.config(text = "Description", command = lambda: Apply(POPUP, "Description"))

    # Bind Buttons
    # Enter
    Button_POPUP_01.bind("<Enter>", Enter_Widget)
    Button_POPUP_02.bind("<Enter>", Enter_Widget)
    Button_POPUP_03.bind("<Enter>", Enter_Widget)
    Button_POPUP_04.bind("<Enter>", Enter_Widget)

    # Leave
    Button_POPUP_01.bind("<Leave>", Leave_Widget)
    Button_POPUP_02.bind("<Leave>", Leave_Widget)
    Button_POPUP_03.bind("<Leave>", Leave_Widget)
    Button_POPUP_04.bind("<Leave>", Leave_Widget)

    # Place the Buttons
    Button_POPUP_01.place(relheight = 0.3, relwidth = 0.3, relx = 0.1, rely = 0.1)
    Button_POPUP_02.place(relheight = 0.3, relwidth = 0.3, relx = 0.6, rely = 0.1)
    Button_POPUP_03.place(relheight = 0.3, relwidth = 0.3, relx = 0.1, rely = 0.6)
    Button_POPUP_04.place(relheight = 0.3, relwidth = 0.3, relx = 0.6, rely = 0.6)

def Database(Type):

    # Declaring Variables
    count = 0
    Data_Database = []

    # Pull the data out of the database
    Data_Database = Query(Type)

    # Place info in the Treeview
    for record in Data_Database:
        if count % 2 == 0:
            Tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[3], record[2], record[1]), tags=('evenrow',))
        else:
            Tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[3], record[2], record[1]), tags=('oddrow',))
        count += 1

    # Config Widgets
    # Config Label
    Label01.config(text = "Database")

    # Config Buttons
    Button01.config(text = "Back", command = Home_Page)
    Button02.config(text = "Filter", command = Filter)

    # Place Widgets
    # Treeview
    Tree_Frame.place(relheight = 0.6, relwidth = 0.8, relx = 0.1, rely = 0.2)

    # Buttons
    Button01.place(relheight = 0.1, relwidth = 0.2, relx = 0.1, rely = 0.85)
    Button02.place(relheight = 0.1, relwidth = 0.2, relx = 0.7, rely = 0.85)

def Select_File():
    App.withdraw()
    File_Path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
    App.deiconify()
    with open(File_Path, 'r') as File_Readed:
        File_Data = json.load(File_Readed)
    return File_Data

def Check_Civ():

    Hide_Widgets()

    Data_Json = Select_File()

    Data_Database = Query("Normal")

    results = []
    results_stack = 0
    stacking_list = []
    counter00 = 0

    while counter00 < len(Data_Json["bonuses"][0]):
        if "and" in Data_Database[Data_Json["bonuses"][0][counter00]][3]:
            Temporary_List_Splitted_Bonus = [Data_Database[Data_Json["bonuses"][0][counter00]][3].split(" and ")]
            counter01 = 0
            while counter01 < len(Temporary_List_Splitted_Bonus[0]):
                stacking_list += [Temporary_List_Splitted_Bonus[0][counter01]]
                counter01 += 1
        else:
            stacking_list += [Data_Database[Data_Json["bonuses"][0][counter00]][3]]
        counter00 += 1

    for items in Data_Json["bonuses"][0]:
        counter00 = 0
        while True:
            if items+1 == Data_Database[counter00][0]:
                results += [Data_Database[counter00][2]]
            counter00 += 1
            if counter00 == len(Data_Database):
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

    text02 = str(Data_Json["alias"] + "\n\n")
    for items in Data_Json["bonuses"][0]:
        text02 += str(Data_Database[items][3] + ", ") + str(Data_Database[items][2]) + ", " + str(Data_Database[items][1] + "\n")

    text02 += "\nStacking Penalty: " + str(results_stack)

    if "UNAVALIBLE" in stacking_list:
        text01 = "This civ has got the one civ bonus which is ilegal, Long Swordsman, Two-Handed Swordsman upgrades available one age earlier"

    List_Banned_Team_Bonus = [69, 70, 71, 72, 73]
    for items in Data_Json["bonuses"][4]:
        if items in List_Banned_Team_Bonus:
            text01 = "This civ has one of the 5 unavalible Team Bonus"
            break

    # Config Widgets
    Label01.config(text = "Cheking Civs")
    Label02.config(text = text02 + "\n\n\n\n\n" + text01)

    # Config Buttons
    Button01.config(text = "Back", command = Home_Page)
    Button02.config(text = "Check Another", command = Check_Civ)

    # Place Widgets
    # Labels
    Label02.place(relheight = 0.7, relwidth = 0.8, relx = 0.1, rely = 0.2)

    # Buttons
    Button01.place(relheight = 0.1, relwidth = 0.2, relx = 0.2, rely = 0.85)
    Button02.place(relheight = 0.1, relwidth = 0.2, relx = 0.6, rely = 0.85)


def Home_Page():

    # Hide Widgets
    Hide_Widgets()
    
    # Config the Buttons
    Button01.config(text = "Database", command = lambda: Database("Normal"))
    Button02.config(text = "Check Civ", command = Check_Civ)

    # Config the Label
    Label01.config(text = "Civ Checker")

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

# Create Labels
Label01 = Label(App, font = "Arial 50", justify = "center", foreground = "#0097FF", relief = "flat")
Label02 = Label(App, font = "Arial 12", justify = "left", foreground = "#1544F1", relief = "flat")

# Create Buttons
Button01 = Button(App, background = "#0097FF", foreground = "#D9D9D9", activebackground = "#000CFF", activeforeground = "#D9D9D9", relief = "flat", font = "Arial 16")
Button02 = Button(App, background = "#0097FF", foreground = "#D9D9D9", activebackground = "#000CFF", activeforeground = "#D9D9D9", relief = "flat", font = "Arial 16")

# Create Tree Frame
Tree_Frame = Frame(App)

# Create Treeview Style
Style01 = ttk.Style()
Style01.map('Treeview', background = [('selected', '#000CFF')], foreground = [("selected", "#D9D9D9")])

# Create Treeview 
Tree = ttk.Treeview(Tree_Frame, style = "Treeview")

# Add columns
Tree["columns"] = ("Column01", "Column02", "Column03", "Column04")
Tree.column("#0", width=0, stretch = 0)
Tree.column("Column01", width = 5)
Tree.column("Column02", width = 5)
Tree.column("Column03", width = 5)
Tree.column("Column04", width = 10)

# Add headings
Tree.heading("#0", text="")
Tree.heading("Column01", text="Bonus ID")
Tree.heading("Column02", text="Bonus Type")
Tree.heading("Column03", text="Bonus Cost")
Tree.heading("Column04", text="Bonus Description")

# Configure stripped rows
Tree.tag_configure("oddrow", background="#D9D9D9", foreground = "#0097FF")
Tree.tag_configure("evenrow", background="#0097FF", foreground = "#D9D9D9")

# Place the Tree in the Frame
Tree.place(relheight = 1, relwidth = 1, relx = 0, rely = 0)

Tree.column("Column02", width = 100)
Tree.column("Column04", width = 400)

# Place the binding in the Widgets
# Enter
Button01.bind("<Enter>", Enter_Widget)
Button02.bind("<Enter>", Enter_Widget)

# Leave
Button01.bind("<Leave>", Leave_Widget)
Button02.bind("<Leave>", Leave_Widget)


# Run Home Page
Home_Page()

# Make App run
App.mainloop()