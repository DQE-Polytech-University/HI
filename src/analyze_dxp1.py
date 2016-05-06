from tkinter import *

def show_entry_fields():
   print("our text: %s\n" % (e1.get()))

master = Tk()
master.title("cryptography")
Label(master, text="our text").grid(row=0)

e1 = Entry(master)

e1.grid(row=0, column=1)

Button(master, text='Quit', command=master.quit).grid(row=2, column=0, sticky=W, pady=4)
Button(master, text='Show', command=show_entry_fields).grid(row=2, column=1, sticky=W, pady=4)

mainloop( )

