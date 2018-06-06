from Tkinter import *
import Tkinter as ttk
from ttk import *
from graphics import *
import math
import os
import os.path
from cStringIO import StringIO
import sys
import fileinput

PATH = '' #path to your vip.cfg file
def select():
    choice = var.get()
    if choice == "V.I.P":
        addvip()
root = Tk()
root.title("Staff Panel")
var = StringVar(root)
var.set('Choose')
choices = ['','V.I.P']
option = OptionMenu(root, var, *choices)
option.pack(side='left', padx=10, pady=10)
button = Button(root, text="Add", command=select)
button.pack(side='left', padx=20, pady=10)
def mainscreen():
    win = GraphWin("Staff Panel", 500, 500)
    
    mes = Text(Point(250,250), "Staff Panel Unfinished")
    mes1 = Text(Point(250, 262), "Note that i wont do any updates in the future")
    mes2 = Text(Point(250, 274), "If you have troubles working with this you can add me on Steam")
    mes.setFace('courier')
    mes1.setFace('courier')
    mes2.setFace('courier')
    mes2.setSize(10)
    mes.draw(win)
    mes1.draw(win)
    mes2.draw(win)
    root.mainloop()
    win.getMouse()
    win.close()
def inCircle(pt1, circ):
    dx = pt1.getX() - circ.getCenter().getX()
    dy = pt1.getY() - circ.getCenter().getY()
    dist = math.sqrt(dx*dx + dy*dy)
    return dist <= circ.getRadius()
def addvip():
    win = GraphWin("AddVIP", 500,500)
    
    box_input = Entry(Point(250,265), 20)

    box_input.draw(win)

    txt = Text(Point(250,280), "")
    txt.setFace('courier')
    txt.draw(win)

    mes = Text(Point(250, 230), "Put in the SteamID of the Person you want to add\n Click the window to update the input box")
    mes.setFace('courier')
    mes.setSize(10)
    mes.draw(win)

    mes1 = Text(Point(250, 325), "Add")
    mes1.setFace('courier')
    mes1.setSize(20)
    mes1.draw(win)
    
    circ = Circle(Point(250,325), 35)
    circ.draw(win)
    while True:
        txt.setText(box_input.getText())
        mouse = win.getMouse()
        steamid = box_input.getText()
        buf = StringIO()
        buf.write('"VIP"\n')
        buf.write('{\n')
        buf.write('"viplist"\n')
        buf.write('{\n')
        buf.write('"')
        buf.write(steamid)
        buf.write('"')
        buf.write('\n')
        buf.write('}\n')
        buf.write('}')
        delete = buf.getvalue()
        if inCircle(mouse,circ):
            if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
                #if the file already exists write the steamid in it
            else:
                f = open("vip.cfg", "w")
                f.write(str(delete))
                f.close()
mainscreen()
