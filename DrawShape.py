import turtle

def draw_miniGreenTriangle(some_turtle):
    some_turtle.right(60)
    some_turtle.forward(30)
    some_turtle.right(120)
    some_turtle.forward(30)
    some_turtle.right(120)
    some_turtle.forward(30)

def draw_oneset(tuffy):
    tuffy.begin_fill()
    draw_miniGreenTriangle(tuffy)    
    tuffy.penup()
    tuffy.right(120)
    tuffy.forward(30)
    tuffy.left(60)
    tuffy.pendown()
    draw_miniGreenTriangle(tuffy)
    tuffy.penup()
    tuffy.left(120)
    tuffy.forward(30)
    tuffy.right(180)
    tuffy.pendown()
    draw_miniGreenTriangle(tuffy)
    tuffy.end_fill()

def draw_largerModule(some_turtle3,headvalue,posvalue):
    for i in range(0,4):
        some_turtle3.penup()
        some_turtle3.setpos(posvalue)
        some_turtle3.setheading(headvalue)        
        some_turtle3.forward(60*i)
        some_turtle3.pendown()
        draw_oneset(some_turtle3)
    
def draw_mainShape():
    window = turtle.Screen()
    window.bgcolor = 'white'        
    basicTurtle = turtle.Turtle('turtle')
    basicTurtle.speed(10)
    basicTurtle.color('blue')
    basicTurtle.fillcolor('green')
    draw_largerModule(basicTurtle,0,(0,0))   
    for i in range(0,2):
        basicTurtle.back(30)
        basicTurtle.left(60)
        newpos = basicTurtle.pos()
        newhead = basicTurtle.heading()
        draw_largerModule(basicTurtle,newhead,newpos)
    window.exitonclick()      
   
draw_mainShape()
