'''
Created on May 28, 2019

@author: sihuh
'''
import turtle as t
import math
import random

Screen = t.Screen()
Screen.bgcolor('silver')
Screen.tracer(2)


myboundry = t.Turtle()
myboundry.penup()
myboundry.setposition(-400, 400)
myboundry.pendown()
myboundry.pensize(3)
for side in range(4):
    myboundry.forward(800)
    myboundry.right(90)
myboundry.hideturtle()

shapes = ['arrow', 'blank', 'circle','square', 'triangle']
colors = ['red', 'blue','purple','white','pink','yellow','green','orange','brown']

planesnumber = 15
planes = []
for count in range(planesnumber):
    s= random.randint(0,4)
    c = random.randint(0,8)
    
    
    planes.append(t.Turtle())
    planes[count].shape(shapes[s])
    planes[count].color(colors[c])
    planes[count].penup()
    planes[count].speed(0)
    planes[count].setposition(random.randint(-400,400) , random.randint(300,390))
    

    
        

p = t.Turtle()
p.shape('classic')
p.turtlesize(5,5)
p.penup()
p.setposition(0 , -250)
p.left(90)

def move_right():
    x = p.xcor()
    y = p.ycor()
    
    if x <= 400:
        p.setposition(x + 10, y)
  
    
        
  
    
def move_left():
    x = p.xcor()
    y = p.ycor()
    
    if x >= -400:
        p.setposition(x - 10, y)

def reset():
    p.setposition(0,-250)    
    
    
Screen.listen()
Screen.onkeypress(move_right,'Right')
Screen.onkeypress(move_left,'Left')
Screen.onkeypress(reset, 'r')

while True:
    
    for count in range(planesnumber):
        planes[count].forward(3)
        x1 = p.xcor()
        y1= p.ycor()
        
        x2 = planes[count].xcor()
        y2 = planes[count].ycor()
        
        if x2 < -400 or  x2 > 400:
            planes[count].right(180)
    
        if y2 < -400 or  y2 > 400:
            planes[count].right(180)
    
    
    
    
    




































































































t.mainloop()