import turtle

screen = turtle.Screen()
screen.title("Ping Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)


#bottom
pluck = turtle.Turtle()
pluck.speed(0)
pluck.shape("square")
pluck.color("yellow")
pluck.shapesize(stretch_wid=0.5, stretch_len=4)
pluck.penup()
pluck.goto(0,-250)


#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 5
ball.dy = -5

def pluck_right():
    xcor = pluck.xcor()
    xcor = xcor + 10
    pluck.setx(xcor)

def pluck_left():
    xcorneg = pluck.xcor()
    xcorneg = xcorneg - 10
    pluck.setx(xcorneg)    






screen.listen()
screen.onkeypress(pluck_right, "d")
screen._onkeypress(pluck_left, "a")








#the main game loop
while True:
    screen.update()


    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    

#border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1 

    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1 

    elif ball.xcor() > 290:
        ball.setx(290)
        ball.dx *= -1 


    if ball.xcor() < -290:
        ball.setx(-290)
        ball.dx *= -1

    if ball.ycor() > 390:
        ball.goto(0,0)
        ball.dy *=-1

    if ball.ycor() < -390:
        ball.goto(0,0)
        ball.dy *=-1


    #collison
    if ball.ycor() > -300 and (ball.xcor() < pluck.xcor() - 40) and (ball.xcor() > pluck.xcor() -40):
        ball.dy *= 1

    

  

   


    


  

 
