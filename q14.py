from tkinter import Canvas, Tk

root=Tk()

root.title("Scenary Drawing")
root.geometry("800x480")

c=Canvas(root,bg="skyblue",height=480,width=820)
c.pack()

id=c.create_rectangle(0,400,800,480,width=2,fill="brown")

for i in range(0,800,100):
    id=c.create_arc(0+i,450,100+i,350,width=2,start=0,extent=180,outline="black",style="pieslice",fill="green1")
    id=c.create_polygon(548,275,630,200,700,275,width=2,fill="yellow",outline="black")
    id=c.create_rectangle(700,400,550,275,width=2,outline="black",fill="brown1")
    id=c.create_rectangle(600,400,650,350,width=2,outline="black",fill="yellow")

root.mainloop()
