# No explanation cuz even I have no clear idea why or how this works
# I just kept googling and fixed errors and this works :)

import tkinter as t

root = t.Tk()

coord = 10,10,200,200

arc1_canvas = t.Canvas(root, width= 200, height=200)
arc1 = arc1_canvas.create_arc(coord, start=0, extent = 60 , width=1, fill = 'purple1')
arc1_canvas.grid(row=0, column=0)

arc2_canvas = t.Canvas(root, width= 200, height=200)
arc2 = arc2_canvas.create_arc(coord, start=0, extent = 90, width=1, fill = 'purple2')
arc2_canvas.grid(row=0, column=1)

arc3_canvas = t.Canvas(root, width= 200, height=200)
arc3 = arc3_canvas.create_arc(coord, start=0, extent = 135, width=1, fill = 'purple3')
arc3_canvas.grid(row=0, column=2)

arc4_canvas = t.Canvas(root, width= 200, height=200)
arc4 = arc4_canvas.create_arc(coord, start=0, extent = 215, width=1, fill = 'SlateBlue1')
arc4_canvas.grid(row=1, column=0)

arc5_canvas = t.Canvas(root, width= 200, height=200)
arc5 = arc5_canvas.create_arc(coord, start=0, extent = 270, width=1, fill = 'SlateBlue2')
arc5_canvas.grid(row=1, column=1)

arc6_canvas = t.Canvas(root, width= 200, height=200)
arc6 = arc6_canvas.create_arc(coord, start=0, extent = 310, width=1, fill = 'SlateBlue3')
arc6_canvas.grid(row=1, column=2)

root.mainloop()
