import tkinter as tk
from tkinter import *
from tkinter import ttk

# Creating tkinter window
window = tk.Tk()
window.geometry('350x250')
# Label
ttk.Label(window, text="Select a Fighter :",
          font=("Times New Roman", 10)).grid(column=0,
                                             row=15, padx=10, pady=25)

n = tk.StringVar()
fighterChosen = ttk.Combobox(window, width=27,
                            textvariable=n)

# Adding combobox drop down list
fighterChosen['values'] = (' Path of the Mountain',
                          ' Birth of the Protector',
                          ' Return of the Scout',
                          ' Rise of the Warrior')

fighterChosen.grid(column=1, row=15)

# Shows february as a default value
fighterChosen.current(1)

# Create a Button
btn = Button(window, text='Click me !', bd='5',
             command=window.destroy)

# Set the position of button on the top of window.
# btn.pack(side='bottom')

# Create text widget and specify size.
T = Text(window, height=5, width=52)

# Create label
l = Label(window, text="Fact of the Day")
l.config(font=("Courier", 14))

Fact = """A man can be arrested in 
Italy for wearing a skirt in public."""

# Create button for next text.
b1 = Button(window, text="Next", )

# Create an Exit button.
b2 = Button(window, text="Exit",
            command = window.destroy)

#l.pack()
# T.pack()
# b1.pack()
# b2.pack()

# Creating Menubar
menubar = Menu(window)

# Adding File Menu and commands
file = Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=file)
file.add_command(label='New File', command=None)
file.add_command(label='Open...', command=None)
file.add_command(label='Save', command=None)
file.add_separator()
file.add_command(label='Exit', command=window.destroy)

# Adding Edit Menu and commands
edit = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Edit', menu=edit)
edit.add_command(label='Cut', command=None)
edit.add_command(label='Copy', command=None)
edit.add_command(label='Paste', command=None)
edit.add_command(label='Select All', command=None)
edit.add_separator()
edit.add_command(label='Find...', command=None)
edit.add_command(label='Find again', command=None)

# Adding Help Menu
help_ = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Help', menu=help_)
help_.add_command(label='Tk Help', command=None)
help_.add_command(label='Demo', command=None)
help_.add_separator()
help_.add_command(label='About Tk', command=None)

# display Menu
window.config(menu=menubar)
mainloop()
# Insert The Fact.
T.insert(tk.END, Fact)

window.mainloop()