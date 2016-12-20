import turtle

def draw_square(some_turtle):
    #this is a loop to create a square iwith the instance some turtle
    for x in range (0,4):
        some_turtle.forward (100)
        some_turtle.right(90)

#draw_shape is only calling the square and line function for now. 
def draw_shapes():
    #This opens a window for the function turtle 
    window = turtle.Screen()
    window.bgcolor("red")
    #This is to name (heidi) and shape, color my turtle and start moving it
    heidi = turtle.Turtle()
    heidi.shape("circle")
    heidi.color("yellow")
    heidi.speed(0)
    for x in range (0,36):
        draw_square(heidi)
        heidi.right(10)
    draw_line()
    write_initials()
    #this is to close the window
    window.exitonclick()

#Adding some additional functions to be creative and try some changes
def draw_line():        
    #this is to create another turtle named mike and creates a line downwards
    mike = turtle.Turtle()
    mike.shape("arrow")
    mike.color("blue")
    mike.right(90)
    mike.forward(350)

def write_initials():
    #this will write an initial of H in black
     h=turtle.Turtle()
     h.shape("turtle")
     h.color("black")
     #
     h.penup()
     h. setpos(150,-250)
     h.pendown()
     h.right(90)  
     h.forward(100)
     #
     h.penup()
     h. setpos(150,-300)
     h.pendown()
     h.left(90)
     h.forward(50)
     #
     h.penup()
     h. setpos(200,-250)
     h.pendown()
     h.right(90)  
     h.forward(100)  
    
def draw_circle():        
    #this is to create another turtle named vale and creates a circle
    vale = turtle.Turtle()
    vale.shape("arrow")
    vale.color("pink")
    vale.circle(100)

def draw_triangle():
    #this is to create another turtle named sarah and creates a triangle
    sarah = turtle.Turtle()
    sarah.shape("turtle")
    sarah.color("black")
    for y in range (0,3):
        sarah.forward (50)
        sarah.left(120)
    #this is to close the window on a click
    #window.exitonclick()
        
draw_shapes()

