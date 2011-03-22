#Jill Lee
#Sunday Jan 30, 2011
#The Automatic Ad Generator generates ads automatically using the name and slogan submitted by the user and randomly mixed colors.
#This code depends on John Zelle's graphics.py.
#Mar 19 updated version

from graphics import *
from random import randrange

#Window 1: User inputs
win = GraphWin('Automatic Ad Generator',500,200)

def courier(text):
    text.setFace('courier')
    text.setSize(10)

#This is the direction for the user to enter a name and slogan.
intro=Text(Point(250,25),"Enter a name and slogan you'd like in your ad.\nClick the window when ready.")
courier(intro)

#Leading to the name field
query_name=Text(Point(158,100),"Name:")
courier(query_name)

#Name field proper
input_name=Entry(Point(278,100),20)
input_name.setText('BP')
courier(input_name)

#Leading to slogan field
query_slogan=Text(Point(165,125),"Slogan:")
courier(query_slogan)

#Slogan field proper
input_slogan=Entry(Point(278,125),20)
input_slogan.setText('Beyond Prosecution')
courier(input_slogan)

#Draw draw draw
intro.draw(win)
query_name.draw(win)
input_name.draw(win)
query_slogan.draw(win)
input_slogan.draw(win)

#Click when you're done
win.getMouse()

#Window 2: The output
win2 = GraphWin('Automatic Ad Generator',300,150)
win2.setCoords(0.0,0.0,3.0,1.5)

#Making the rectangles
strip1=Rectangle(Point(0.0,1.5),Point(3.0,0.95))
strip2=Rectangle(Point(0.0,0.95),Point(3.0,0.73))
strip3=Rectangle(Point(0.0,0.73),Point(3.0,0.53))
strip4=Rectangle(Point(0.0,0.53),Point(3.0,0.0))
#Then color them in and draw
def randcolor(box):
    r=randrange(80,222)
    g=randrange(80,222)
    b=randrange(80,222)
    box.setFill(color_rgb(r,g,b))
    box.setOutline(color_rgb(r,g,b))
    box.draw(win2)
randcolor(strip1)
randcolor(strip2)
randcolor(strip3)
randcolor(strip4)

#Get the name and the slogan from the input window
name=Text(Point(1.5,0.85),input_name.getText())
name.setFace('helvetica')
name.setSize(12)
name.setTextColor('white')
name.setStyle('bold')

slogan=Text(Point(1.5,0.64),input_slogan.getText())
slogan.setFace('helvetica')
slogan.setSize(12)
slogan.setTextColor('white')

#Draw draw
name.draw(win2)
slogan.draw(win2)

win.close()
win2.getMouse()
win2.close()
