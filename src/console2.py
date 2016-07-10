from tkinter import *
def Insert():
    	name = text.get()
    	Text.insert(END, name)
    	text.delete(0,END)	
    
root = Tk()
root.title(u'Encrypt me =P')
root.resizable(False, False)
root.geometry('600x400')
 
text1 = Entry(root, bg = 'white')
text2 = Entry(root, bg = 'white')

Text = Listbox(root,height=170,width=170,bd=0)

listbox1=Listbox(root,height=6,width=20,selectmode=EXTENDED)
list1=["Hadamard","NOT","Gate_pi","Gate_pi8","Gate_turn","CNOT"]
for i in list1:
    listbox1.insert(END,i)
listbox1.pack()
listbox1.place(x=400, y=35) 


Text.pack()
text1.pack()
text2.pack()
Text.place(x=0, y= 130)  
text1.place(x=230, y=10) 
text2.place(x=230, y=40) 


def delete():
  Text.delete(0,END)
Text = Listbox(Text)
Text.pack()


  
Button1 = Button(root, text="Enter the number of bases:", width=30, command=Insert)
Button2 = Button(root, text="Enter the length of the message:", width=30, command=Insert)
Button3 = Button(root, text="Clear", width=30, command=delete)
Button4 = Button(root, text='Exit', width=30, command=root.destroy)
Button5 = Button(root, text="Select gate:", width=16)


Button1.pack()
Button2.pack()
Button3.pack()
Button4.pack()
Button5.pack()
Button1.place(x=0, y=5)
Button2.place(x=0, y=35)
Button3.place(x=0, y=65)
Button4.place(x=0, y=95)
Button5.place(x=400, y=5)

root.mainloop()
  	


