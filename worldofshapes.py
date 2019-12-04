def start_again():
##function clears the screen and returns turtle to home position.
##This is a void function
    t.penup()
    t.home()  
    t.clear()
    
def random_color():
##function generates a random color.
##This function returns generated color as a tuple
    red = r.randint(0,255)
    green = r.randint(0,255)
    blue = r.randint(0,255)
    generated_color = (red,green,blue)
    return generated_color

def square_with_color(side,color):
##function draws a square with length side and fills it with color.
##This is a void function
    t.fillcolor(color)
    t.begin_fill()
    t.pendown()
    for i in range(4):
        t.forward(side)  
        t.left(90)
    t.end_fill()
    

def triangle_with_color(side,color):
##function draws an equilateral triangle with length side and fills it with color.
##This is a void function
    t.fillcolor(color)
    t.begin_fill()
    t.pendown()
    for i in range (3):
        t.forward(side)
        t.left(120)
    t.end_fill()

def circle_with_color(radius,color):
##function draws an circle with radius and fills it with color.
##This is a void function
    t.fillcolor(color)
    t.begin_fill()
    t.pendown()
    t.circle(radius)
    t.end_fill()

def rectangle_with_color(length,breadth,color):
##function draws a rectangle with given length and breadth and fills it with color.
##This is a void function'
    t.fillcolor(color)
    t.begin_fill()
    t.pendown()
    for i in range(2):
        t.forward(length) 
        t.left(90)
        t.forward(breadth)
        t.left(90)
    t.end_fill()    

def begin_anew():
##function takes turtle to the left edge of the screen
##This is a void function    
    t.penup()
    t.goto(-width/2,-height/2)
    t.pendown()    
    

## TOP LEVEL

import turtle as t
import random as r

t.title(" world of shapes") #title for turtle window
t.colormode(255)
t.speed(8) #setting speed of turtle

#setting width and height of turtle window
width=600
height=600
t.setup (width, height, startx=0, starty=0)

#welcome message
delay=1500
t.goto(0,0)
t.write("\n Welcome to the world of shapes!", align="center", font=("Showcard Gothic", 18, "bold"))
t.penup()
t.fd(delay)

##drawing squares
start_again()
begin_anew()
square_with_color(width,random_color())
w_count=width
for i in range(5): #making 5 squares one inside the other
    t.penup()
    t.fd(50)
    t.left(90)
    t.fd(50)
    t.right(90)
    w_count = w_count-100
    t.pendown()
    square_with_color(w_count,random_color())
t.penup()
t.goto(0,0) #writing title for page
t.pendown()
t.write("WORLD OF SQUARES", align="center", font=("Showcard Gothic", 36, "bold"))
t.penup()
t.fd(delay)

####drawing triangles
start_again()
begin_anew()
triangle_with_color(width,random_color())
w_count=width
for i in range(5): #making 5 triangles one inside the other
    t.penup()
    t.fd(50)
    t.left(90)
    t.fd(30)
    t.right(90)
    w_count = w_count-100
    t.pendown()
    triangle_with_color(w_count,random_color())
t.penup()
t.goto(0,0) #writing title for page
t.pendown()
t.write("WORLD OF TRIANGLES", align="center", font=("Showcard Gothic", 36, "bold"))
t.penup()
t.fd(delay)

##drawing rectangles
start_again()
begin_anew()
rectangle_with_color(width,height,random_color())
w_count=width
h_count=height
for i in range(4):#making 4 triangles one inside the other
    t.penup()
    t.fd(20)
    t.left(90)
    t.fd(50)
    t.right(90)
    w_count = w_count-50
    h_count=h_count-120
    t.pendown()
    rectangle_with_color(w_count,h_count,random_color())
t.penup()
t.goto(0,0) #writing title for page
t.pendown()
t.write("WORLD OF RECTANGLES", align="center", font=("Showcard Gothic", 36, "bold"))
t.penup()
t.fd(delay)


##drawing circles
start_again()
t.goto(0,-300)
radius=width/2
t.speed(10)
circle_with_color(radius,random_color())
w_count=radius

for i in range(12): #making circles one inside the other
    t.penup()
    t.left(90)
    t.fd(50)
    t.right(90)
    w_count = w_count-50
    t.pendown()
    circle_with_color(w_count,random_color())
t.penup()
t.goto(0,0) #writing title for page
t.pendown()
t.write("WORLD OF CIRCLES", align="center", font=("Showcard Gothic", 36, "bold"))
t.penup()
t.fd(delay)

#goodbye message
start_again()
t.goto(0,0)
t.write("\n HOPE YOU ENJOYED IT! BYE!!", align="center", font=("Showcard Gothic", 18, "bold"))
t.penup()
t.fd(delay)

#t.bye() #shut down turtle screen
