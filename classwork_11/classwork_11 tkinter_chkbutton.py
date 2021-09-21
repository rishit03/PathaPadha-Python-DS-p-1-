from tkinter import *
from tkinter import messagebox

root = Tk()

chk1=IntVar()
chk2=IntVar()
chk3=IntVar()

ch1 = Checkbutton(root,text="Python",variable=chk1,offvalue=0,onvalue=1)
ch2 = Checkbutton(root,text="Java",variable=chk2,offvalue=0,onvalue=1)
ch3 = Checkbutton(root,text="C++",variable=chk3,offvalue=0,onvalue=1)

ch1.pack()
ch2.pack()
ch3.pack()

root.mainloop()
