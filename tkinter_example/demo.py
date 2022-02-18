from tkinter import *

def onClick():
    # accesses the global label2 widget
    global label2 
    # destroys the existing label
    label2.destroy() 
    text = entry1.get()
    # reassigns global widget with label containing text
    label2 = Label(root, text=text, background='White', padx=1.5, pady=2, relief='ridge') 
    # displays on the window
    label2.grid(row=2, column=2) 

root = Tk()

label1 = Label(root, text = "Enter message", background='White', padx=1.5, pady=2)
label1.grid(row=1, column=1)

button1 = Button(root, text='Click me!', command = onClick)
button1.grid(row=2, column=1)

entry1 = Entry(root)
entry1.grid(row=1, column=2)

# Creates a label with empty text which will be filled in later on
label2 = Label(root, text='', background='White', padx=1.5, pady=2, relief='ridge') 

root.mainloop()