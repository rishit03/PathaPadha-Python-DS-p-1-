import tkinter
from tkinter import messagebox

def show():
    n1=int(e1.get())
    n2=int(e2.get())
    result=n1+n2
    messagebox.showinfo("Details",result)

def show2():
    n1=int(e1.get())
    n2=int(e2.get())
    result2=n1-n2
    messagebox.showinfo("Details",result2)

def show3():
    n1=int(e1.get())
    n2=int(e2.get())
    result3=n1*n2
    messagebox.showinfo("Details",result3)

def show4():
    n1=int(e1.get())
    n2=int(e2.get())
    result4=float(n1/n2)
    messagebox.showinfo("Result",result4)
    
root = tkinter.Tk()

l=tkinter.Label(root,text="Enter first number")
l2=tkinter.Label(root,text="Enter second number")
e1=tkinter.Entry(root)
e2=tkinter.Entry(root)
b=tkinter.Button(root,text="+",command=show)
b2=tkinter.Button(root,text="-",command=show2)
b3=tkinter.Button(root,text="x",command=show3)
b4=tkinter.Button(root,text="/",command=show4)
l.grid(row=0,column=0)
l2.grid(row=1,column=0)

e1.grid(row=0,column=1)
e2.grid(row=1,column=1)

b.place(x=20,y=42)
b2.place(x=70,y=42)
b3.place(x=120,y=42)
b4.grid(row=3,column=1)

root.mainloop()
