import turtle

t = turtle.Turtle()
turtle.Screen().bgcolor("black")

screen = turtle.Screen()
t.pensize(10)

def Square():
    t.color("blue")
    t.begin_fill()
    t.forward(100)
    t.setheading(90)
    t.forward(100)
    t.forward(100)
    t.setheading(180)
    t.forward(200)
    t.setheading(270)
    t.forward(200)
    t.setheading(0)
    t.forward(100)
    t.end_fill()
     

screen.onkey(Square, "s")
screen.listen()

def triangle():
    t.color("red")

    t.penup()
    t.setheading(50)
    t.forward(100)
    t.pendown()
    t.setheading(180)
    t.setheading(90)
    t.penup()
    t.forward(150)
    t.setheading(0)
    t.pendown()
    t.begin_fill()
    t.forward(265)
    t.setheading(125)
    t.forward(284)
    t.setheading(225)
    t.forward(330)
    t.setheading(360)
    t.forward(150)
    t.end_fill()
  
    
    
    

screen.onkey(triangle, "t")
screen.listen()

def sirkul():
    t.color("white")
    t.begin_fill()
    t.penup()
    t.goto (220, 10)
    t.pendown()
    t.circle(100)
    t.end_fill()
    

screen.onkey(sirkul, "c")
screen.listen()

def bituin():
    t.color("yellow")
    t.begin_fill()
    t.penup()
    t.goto(20, -150)
    t.pendown()
    for _ in range(5):  
        t.forward(200)  
        t.left(144)
    t.end_fill()

screen.onkey(bituin, "b")
screen.listen()
