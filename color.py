import tkinter as tk

global rets 

rets="black"




class myapps:
    def __init__(self,root:tk.Tk):
        self.root=root
        self.root.title("color select")
        self.colors=["black","blue","red","magenta","green","cyan","yellow","gray","darkgray","lightblue","darkred","darkmagenta","lightgreen","lightcyan","lightyellow","lightgray"]
        self.root.geometry("640x480")
        self.root.configure(background="black")
        self.canvas=tk.Canvas(background="black",width=640,height=480)
        self.canvas.pack(padx=0,pady=0)
        c=self.canvas
        self.canvas.bind("<Button-1>",self.clicks)
        for x in range(0,8):
            aa=640//8
            a=aa*x
            for y in range(0,2):
                bb=480//2
                b=bb*y
                c.create_rectangle(a,b,a+(640/8),b+(480//2),fill=self.colors[x+y*8])
    def clicks(self,event):
        global rets
        x=event.x
        y=event.y
        x=x//(640//8)
        y=y//(480//2)
        xy=x+y*8
        if xy<16:
            rets=self.colors[xy]
        self.root.quit()




def getcolor():
    root=tk.Tk()
    apps=myapps(root)
    root.mainloop()
    return rets




print(getcolor())