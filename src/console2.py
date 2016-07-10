from tkinter import *
import numpy as np
import math
import Classes as hi
def Insert():
    	name = text1.get()
    	Text1.insert(END, name)
    	text.delete(0,END)
     
def Key_issue():
    bases = text1.get()
    long_message = text2.get()
    bb84 = hi.Various_measurement(int(bases),int(long_message),0)
    bb84.begin()
    bb84.compare_bob_alice()
    bb84.generate_key()
    key = bb84.key
    Text1.insert(END, key)
    #text.delete(0,END)
    
root = Tk()
root.title('Encrypt me =P')
root.resizable(False, False)
root.geometry('800x550')
 
text1 = Entry(root, bg = 'white')
text2 = Entry(root, bg = 'white')

Text1 = Listbox(root,height=15,width=35,bd=0)
Text2 = Listbox(root,height=15,width=35,bd=0)


listbox1=Listbox(root,height=6,width=20,selectmode=EXTENDED)
list1=["Hadamard","NOT","Gate_pi","Gate_pi8","Gate_turn","CNOT"]
for i in list1:
    listbox1.insert(END,i)
listbox1.pack()
listbox1.place(x=400, y=35) 

post_user = Text(root,height=10,width=32,font='Arial 14',wrap=WORD)

Text1.pack()
Text2.pack()
text1.pack()
text2.pack()
post_user.pack()


text1.place(x=230, y=10) 
text2.place(x=230, y=40) 
Text1.place(x=400, y= 270)
Text2.place(x=550, y= 270)
post_user.place(x=5, y= 270)

#scrollbar['command'] = Text2.xview
#Text2['yscrollcommand'] = scrollbar.set


def delete():
  Text1.delete(0,END)
Text1 = Listbox(Text1)
Text1.pack()


  
Button1 = Button(root, text="Enter the number of bases:", width=30)
Button2 = Button(root, text="Enter the length of the message:", width=30)
Button3 = Button(root, text="Encrypt message", width=30)
Button4 = Button(root, text="Issue key", width=30, command=Key_issue)
Button5 = Button(root, text="Decrypt message", width=30)
Button6 = Button(root, text="Clear all items", width=30, command=delete)
Button7 = Button(root, text='Exit', width=30, command=root.destroy)
Button9 = Button(root, text="Enter your message:", width=30,bg='green',fg='white')
Button10 = Button(root, text="Our keys:", width=16)
Button11 = Button(root, text="The encrypted message:", width=30)

Button8 = Button(root, text="Select gate:", width=16)


Button1.pack()
Button2.pack()
Button3.pack()
Button4.pack()
Button5.pack()
Button6.pack()
Button7.pack()
Button8.pack()
Button9.pack()
Button10.pack()
Button11.pack()


Button1.place(x=0, y=5)
Button2.place(x=0, y=35)
Button3.place(x=0, y=65)
Button4.place(x=0, y=95)
Button5.place(x=0, y=125)
Button6.place(x=0, y=155)
Button7.place(x=0, y=185)
Button9.place(x=0, y=235)
Button10.place(x=400, y=235)
Button11.place(x=550, y=235)

Button8.place(x=400, y=5)

root.mainloop()
  	


