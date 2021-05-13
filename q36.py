import tkinter as tk
import math
root= tk.Tk()

screen = tk.Canvas(root, width = 600, height = 300)
screen.pack()

heading = tk.Label(root,text='Basic Calculator')
heading.config(font=('Sans Serif',10))
screen.create_window(260,10,window=heading)

n1 = tk.Entry (root) 
screen.create_window(175, 70, window=n1)
n2 = tk.Entry (root) 
screen.create_window(350, 70, window=n2)

btn1 = tk.Button(text='+' ,command=lambda:calculation('+'))
btn2 = tk.Button(text='-' ,command=lambda:calculation('-'))
btn3 = tk.Button(text='*' ,command=lambda:calculation('*'))
btn4 = tk.Button(text='/' ,command=lambda:calculation('/'))
screen.create_window(225,120,window=btn1)
screen.create_window(250,120,window=btn2)
screen.create_window(275,120,window=btn3)
screen.create_window(300,120,window=btn4)

def calculation(op):
    x1 = n1.get()
    x2 = n2.get()
    if op == '+':
        soln = tk.Label(root, text=int(x1)+int(x2))
        screen.create_window(225,170,window=soln)
    if op == '-':
        soln = tk.Label(root, text=int(x1)-int(x2))
        screen.create_window(225,170,window=soln)
    if op == '*':
        soln = tk.Label(root, text=int(x1)*int(x2))
        screen.create_window(225,170,window=soln)
    if op == '/':
        if int(x2)==0:
            soln = tk.Label(root, text=math.inf)
            screen.create_window(225,170,window=soln)
        else:
            soln = tk.Label(root, text=int(x1)/int(x2))
            screen.create_window(225,170,window=soln)

root.mainloop()
