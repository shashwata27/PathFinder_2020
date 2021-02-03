import tkinter as tk
from tkinter import PhotoImage

class getPath(tk.Tk):
    def __init__(self):

        tk.Tk.__init__(self)
        self.title("PathFinder")
        self.geometry('400x50')
        self.resizable(width=False, height=False)
        img = PhotoImage(file=r"C:\Users\santu saha\PycharmProjects\PathFinderActual\pathfin.png")
        self.iconphoto(False, img)

        self.label1 = tk.Label(self, text="Enter the Dimension here: ").grid(row=0, column=0)
        self.e1 = tk.Entry(self, width=50)
        self.e1Grid = self.e1.grid(row=0, column=1)
        self.availer=False
        self.availer2 = False
        self.e1Path=None


        self.submit = tk.Button(self, text='Submit',bg="green", command=self.submit).grid(row=1, column=1)



    def submit(self):
       self.e1Path = self.e1.get()
       self.availer=True

       if self.e1Path!="":#if nothing is entered e1path converts to blank text due to get function
           self.availer2=True
       self.destroy()





