# Basic Tkinter
````
import tkinter as tk
from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter.ttk import Progressbar
from tkinter import filedialog
````
___
## Creating a new window and configurations
````
window = tk.Tk() # create tk object
window.title("Window") # assign name to window object
window.minsize(width=500, height=50) # set size
window.geometry("500x400") # also for size
window.wm_iconbitmap("") # setting the icon for the window
window.config(padx=10, pady=10) # adding some space around thw window, the same can be done for widgets
.config() is used to access an object's attributes after its initialisation
window.mainloop() # allows to visualize the object
````
___
## Geometry managers
### .pack() geometry manager
.pack() one under another the previous can't use with grid()!  
The ```side``` keyword argument of .pack() specifies on which side of the window the widget should be placed.  
tk.TOP  
tk.BOTTOM  
tk.LEFT  
tk.RIGHT  

```fill``` keyword argument to specify in which direction the frames should fill
````
import tkinter as tk

frame = tk.Frame(master=window)
frame2 = tk.Frame(master=window)
frame1.pack(fill=tk.X, side=tk.LEFT)
frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
````
___
### .place() geometry manager

You can use .place() to control the precise location that a widget should occupy in a window or Frame. You must provide two keyword arguments, x and y, which specify the x- and y-coordinates for the top-left corner of the widget. Both x and y are measured in pixels, not text units.

The origin (where x and y are both 0) is the top-left corner of the Frame or window. So, you can think of the y argument of .place() as the number of pixels from the top of the window, and the x argument as the number of pixels from the left of the window.

Layouts created with .place() are not responsive. They don’t change as the window is resized !
````
label1 = tk.Label(master=frame, text="Hello)", bg="red")
label1.place(x=0, y=0)
````
___
### .grid() geometry manager
.grid() works by splitting a window or Frame into rows and columns. You specify the location of a widget by calling .grid() and passing the row and column indices to the row and column keyword arguments. Both row and column indices start at 0, so a row index of 1 and a column index of 2 tells .grid() to place a widget in the third column of the second row. Can't use with pack()!

````
label.grid(column = 0, row = 0)
````

For adding space around the outside of a grid cell we can use:  
- padx adds padding in the horizontal direction.  
- pady adds padding in the vertical direction.

````
frame.grid(row=i, column=j, padx=5, pady=5)
````
You can adjust how the rows and columns of the grid grow as the window is resized using .columnconfigure() and .rowconfigure() on the window object. Remember, the grid is attached to window, even though you’re calling .grid() on each Frame widget. Both .columnconfigure() and .rowconfigure() take three essential arguments:

- The index of the grid column or row that you want to configure (or a list of indices to configure multiple rows or columns at the same time)  
- A keyword argument called weight that determines how the column or row should respond to window resizing, relative to the other columns and rows  
- A keyword argument called minsize that sets the minimum size of the row height or column width in pixels

weight is set to 0 by default, which means that the column or row doesn't expand as the window resizes. If every column and row is given a weight of 1, then they all grow at the same rate. If one column has a weight of 1 and another a weight of 2, then the second column expands at twice the rate of the first

You can change the location of each label inside the grid cell using the sticky parameter. sticky accepts a string containing one or more of the following letters:

| Sticky | Description |
|--------|-------------|
|N | North or Top Center
|S | South or Bottom Center
|E | East or Right Center
|W | West or Left Center
|NW | North West or Top Left
|NE | North East or Top Right
|SE | South East or Bottom Right
|SW | South West or Bottom Left
|NS | NS stretches the widget vertically. However, it leaves the widget centered horizontally.
|EW | EW stretches the widget horizontally. However, it leaves the widget centered vertically.
````
label2.grid(row=1, column=0, sticky="n")
````
___
## Widgets
Some example of widgets

| Widget Class | Description |
|--------------|-------------|
|Label | A widget used to display text on the screen
|Button | A button that can contain text and can perform an action when clicked
|Entry | A text entry widget that allows only a single line of text
|Text | A text entry widget that allows multiline text entry
|Frame | A rectangular region used to group related widgets or provide padding between widgets

### Labels
````
label = Label(window, text = "Hello", font = ("Arial Bold",20), fg='white', bg='black', width=10, height=10)
label.config(text="This is new text")
label.pack()
OR
label.grid(column = 0, row = 0)
OR
label.place(x=0, y=0)
````
___
### Frames
````
import tkinter as tk

window = tk.Tk()
frame = tk.Frame()
frame.pack()

window.mainloop()
````
Frames are best thought of as containers for other widgets. Assign a widget to a frame by setting the widget’s master attribute:
````
frame = tk.Frame()
label = tk.Label(master=frame)
````

Frame widgets can be configured with a relief attribute that creates a border around the frame.
````
tk.FLAT: Has no border effect (the default value).
tk.SUNKEN: Creates a sunken effect.
tk.RAISED: Creates a raised effect.
tk.GROOVE: Creates a grooved border effect.
tk.RIDGE: Creates a ridged effect
````

### Buttons
````
# has to be placed before the button
def action():
    print("Do something")

#calls action() when pressed
button = Button(text="Click Me", bg="blue", fg="white" command=action, font = ("Arial",20))
button.grid(column = 0, row = 2) # # puts it in the second column of the window
````
___
### Entries
````
entry = Entry(width=30)
#Add some text to begin with
entry.insert(END, string="Some text to begin with.")
#Gets text in entry
print(entry.get())
entry.pack()

# with entry you can
Retrieving text with .get()
Deleting text with .delete()
Inserting text with .insert()

# set focus to entry widget -> can write text right away
entry.focus()

# Disable entry widget
entry = Entry(window, width=10, state='disabled')
````
___
### Text
````
text = Text(height=5, width=30)
#Puts cursor in textbox.
text.focus()
#Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
#Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()

# with text you can
Retrieve text with .get()
Delete text with .delete()
Insert text with .insert()
````
___
### Spinbox
````
def spinbox_used():
    #gets the current value in spinbox.
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.grid(column = 0, row = 7)

# you can specify the numbers for the Spinbox
spin = Spinbox(window, values = (3,8,11), width = 5)

# Set the value for Spinbox
var = IntVar()
var.set(36)
spin = Spinbox(window, from_=0, to=100, width=5, textvariable=var)
spin.pack()
````
___
### Scale
````
#Called with current scale value.
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()
````
___
### Checkbutton
````
def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())
#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

OR

chk_state = BooleanVar()
chk_state.set(True)
chk = Checkbutton(window, text = 'Choose', var = chk_state)
chk.grid(column = 0, row = 4)
# set the checked state (var=_chk_state) by passing the checkvalue to the checkbutton
````
___
### Radiobutton
````
def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()
````
### Listbox
````
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()
window.mainloop()
````
___
### ScrolledText widget
````
txt = scrolledtext.ScrolledText(window, width = 40, height = 10)
txt.grid(column = 0, row = 6)
# set scrolledtext content
txt.insert(INSERT, 'Your text goes here')
# delete/clear scrolledtext content
# -- txt.delete(1.0, END)
````
___
### Add a combobox widget
````
# -- combo = Combobox(window)
# -- combo['values'] = (1,2,3,4,5, "Text")
# -- combo.current(1)
# -- combo.grid(column = 0, row = 3)
````
___
### Create a MessageBox
````
# -- messagebox.showinfo('Message title', 'Message content')
# -- messagebox.askquestion('Message title', 'Message content') # yes no
# -- messagebox.askyesno('Message title', 'Message content')
# -- messagebox.askokcancel('Message title', 'Message content')
# -- messagebox.askretrycancel('Message title', 'Message content')
messagebox.askyesnocancel('Message title', 'Message content')
# ok, yes, retry returns TRUE
# no, cancel returns FALSE
````
___
### Add a progressbar widget, and change the color
````
# -- style = ttk.Style()
# -- style.theme_use('default')
# -- style.configure("black.Horizontal.TProgressbar", background = 'black')
# -- bar = Progressbar(window, length = 200, style = 'black.Horizontal.TProgressbar')
bar = Progressbar(window, length = 200)
bar['value'] = 70
bar.grid(column = 0, row = 8)
````
___
### Add a file dialog (file and directory chooser)
````
def openfile():
    filedialog.askopenfilenames()
# -- file = filedialog.askopenfilename()
# -- files = filedialog.askopenfilenames() # ask for multiple files
openfiles = Button(window, text = "OpenFiles", bg = "black", fg = "black", command = openfile, font = ("Arial",20))
openfiles.grid(column = 0, row = 9)
````
___
### Specify file types (filter file extensions)
````
def openfile2():
    filedialog.askopenfilename(filetypes = (("Text files","*.txt"),("all files","*.*")))
openfiles2 = Button(window, text = "OpenFiles2", bg = "black", fg = "black", command = openfile2, font = ("Arial",20))
openfiles2.grid(column = 0, row = 10)
````
___
### ask for a directory
````
def openfile3():
    filedialog.askdirectory()
openfiles3 = Button(window, text = "Ask Directory", bg = "black", fg = "black", command = openfile3, font = ("Arial",20))
openfiles3.grid(column = 0, row = 11)
````
___
### specify initial directory for the file dialog by specifying initaldir
````
from os import path
-- file = filedialog.askopenfilename(initialdir= path.dirname(__file__))
````
___
## Example of class
````
import tkinter as tk
from tkinter import scrolledtext

from no_annotation.stirp_annotation import clean_training


class NoAnnotation(tk.Tk):
    def __init__(self):
        super().__init__()

        """Configure root window"""
        self.title("No annotation")
        self.geometry("500x500")

        """ScrolledText widget for the input"""
        self.text_box = scrolledtext.ScrolledText(self, width=100, height=15)
        self.text_box.pack(fill='x')
        self.text_box.insert('1.0', 'Your training goes here')

        """Button strip annotation"""
        self.strip_annotation_button = tk.Button(text="Strip annotation",
                                                 command=self.user_input)
        self.strip_annotation_button.pack()

        """ScrolledText widget for the output"""
        self.text_box2 = scrolledtext.ScrolledText(self, width=100, height=15)
        self.text_box2.pack(fill='x', side=tk.BOTTOM)

    def user_input(self):
        # clean_traaining is a function called from another module
        for i in clean_training(self.text_box.get("1.0", tk.END)):
            self.text_box2.insert('1.0', f"{i}\n")
            
            
if __name__ == '__main__':
    no_an = NoAnnotation()
    no_an.mainloop()
````
___
## Sources used for the creation of this cheat sheet
- D. Amos, Real Python, Python GUI Programming With Tkinter, https://realpython.com/python-gui-tkinter/#controlling-layout-with-geometry-managers
- A. Yu, Master Python by building 100 projects in 100 days, https://www.udemy.com/course/100-days-of-code/
- A. Deviyan, https://gist.github.com/athiyadeviyani/b18afdc8136f003956b1a71d94a6c696
