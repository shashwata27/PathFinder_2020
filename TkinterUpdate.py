#clientside
from tkinter import *

master=Tk()
def click1():
    # btn.config(visible=False)
    Grid.rowconfigure(frame, 0)
    Grid.columnconfigure(frame, 0)
    leb = Label(frame, text="new", bg='yellow')
    leb.grid(row=0, column=0)
    master.update()

frame=Frame(master)
frame.grid(row=0,column=0)

Grid.rowconfigure(frame,0)
Grid.columnconfigure(frame,0)
leb=Label(frame,text="previous",bg='green')

leb.grid(row=0,column=0)

Grid.rowconfigure(frame,1)
Grid.columnconfigure(frame,0)
btn=Button(frame,text="change",bg='blue',command=lambda:click1())

btn.grid(row=1,column=0)


master.mainloop()
