from tkinter import *
from algo import *
from ProMt import *

class App():
    def __init__(self, master,dimension,indexes):
        self.master = master
        self.dimension=dimension
        self.indxes=indexes
        self.maze = [[0] * self.dimension for ze in range(self.dimension)]
        self.cofrm=False


    def Function(self):
        self.master.title("PathFinder")
        self.master.minsize(500, 500)
        img = PhotoImage(file=r"Images\pathfin.png")
        self.master.iconphoto(False, img)

        Grid.rowconfigure(self.master, 0, weight=12)
        Grid.columnconfigure(self.master, 0, weight=12)
        self.frame1 = Frame(self.master)
        self.frame1.grid(row=0, column=0, sticky=N + S + E + W)


        for index in range(self.dimension):
            leb = Label(self.frame1, text=str(index))
            leb.grid(row=0, column=index+1, sticky=N+E+W)
            Grid.rowconfigure(self.frame1, 0, weight=1)
            Grid.columnconfigure(self.frame1, index, weight=1)

        for index in range(self.dimension):
            leb = Label(self.frame1, text=str(index))
            leb.grid(row=index+1, column=0, sticky=W+N+S)
            Grid.rowconfigure(self.frame1, index, weight=1)
            Grid.columnconfigure(self.frame1, 0, weight=1)


        self.gid = []
        for i in range(self.dimension):
            row = []
            Grid.rowconfigure(self.frame1, i + 1, weight=3)
            for j in range(self.dimension):
                Grid.columnconfigure(self.frame1, j + 1, weight=3)
                btn=Button(self.frame1,command=lambda i=i, j=j: self.Click1(i, j))
                btn.grid(sticky=N+S+E+W,padx=2,pady=2,ipadx=1,ipady=1)
                row.append(btn)
                row[-1].grid(row=i + 1, column=j+1)
            self.gid.append(row)


        #frame2 for confrim button
        Grid.rowconfigure(self.master, 1, weight=1)
        Grid.columnconfigure(self.master, 0, weight=1)
        self.frame2 = Frame(self.master)
        self.frame2.grid(row=1, column=0, sticky=N + S + E + W)

        Grid.rowconfigure(self.frame2, 0, weight=1)
        Grid.columnconfigure(self.frame2, 0, weight=1)
        Cbtn=Button(self.frame2,text="Confirm",bg="purple",command=lambda:self.Click2())
        Cbtn.grid(row=0,column=0,padx=10,pady=4,ipadx=3,ipady=1,sticky=N + S + E + W)

        Grid.rowconfigure(self.frame2, 0, weight=1)
        Grid.columnconfigure(self.frame2, 1, weight=1)
        Cbtn = Button(self.frame2, text="Show Path", bg="purple", command=lambda: self.Click3())
        Cbtn.grid(row=0, column=1, padx=10, pady=4, ipadx=3, ipady=1, sticky=N + S + E + W)



    def Click2(self):
        self.cofrm=True


    def Click1(self, i, j):
        self.indxes.append((i,j))
        if len(self.indxes)==1:
            self.gid[i][j]["bg"]="blue"
        elif len(self.indxes)==2:
            self.gid[i][j]["bg"]="green"
        else:
            self.gid[i][j]["bg"] = "black"
            self.maze[i][j] = 1

    def Click3(self):
        if self.cofrm == True:
            path = astar(app.maze, app.indxes[0], app.indxes[1])
            print(path)
            self.showPath(path)
        master.update()


    def showPath(self,path):
        for xe in path:
            self.gid[int(xe[0])][int(xe[1])]["bg"] = "yellow"




if __name__=='__main__':
    app1 = getPath()
    app1.mainloop()
    if app1.availer == True:
        if app1.availer2==True:
            dimension = int(app1.e1Path)
        else:
            quit()
    else:
        quit()

    #dimension = int(input("Enter the dimension: "))
    master = Tk()
    index = []
    app = App(master, dimension, index)
    app.Function()

    master.mainloop()

#print(app.cofrm)
#print(app.maze,app.indxes)
#print(app.indxes)

