import turtle

#ventana
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width = 800, height = 600)
wn.tracer(0)

#marcadores
marA = 0
marB = 0

#jugador1
jA = turtle.Turtle()
jA.speed(0)
jA.shape("square")
jA.color("white")
jA.penup()
jA.goto(-350,0)
jA.shapesize(stretch_wid = 5, stretch_len= 1)

#jugador2
jB = turtle.Turtle()
jB.speed(0)
jB.shape("square")
jB.color("white")
jB.penup()
jB.goto(350,0)
jB.shapesize(stretch_wid = 5, stretch_len= 1)

#pelota
p = turtle.Turtle()
p.speed(0)
p.shape("square")
p.color("white")
p.penup()
p.goto(0,0)
p.dx = 0.2
p.dy = -0.2

#division
div = turtle.Turtle()
div.color("white")
div.goto(0,400)
div.goto(0,-400)

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("JUGADOR A: 0     JUGADOR B: 0", align="center",font=("Courier", 24))

#funciones
#jugador A
def jugadorA_up():
    y = jA.ycor()
    y += 20
    jA.sety(y)

def jugadorA_down():
    y = jA.ycor()
    y -= 20
    jA.sety(y)

#jugador B
def jugadorB_up():
    y = jB.ycor()
    y += 20
    jB.sety(y)

def jugadorB_down():
    y = jB.ycor()
    y -= 20
    jB.sety(y)
    
#teclado
wn.listen()
wn.onkeypress(jugadorA_up,"w")
wn.onkeypress(jugadorA_down,"s")
wn.onkeypress(jugadorB_up,"Up")
wn.onkeypress(jugadorB_down,"Down")


#juego
while True:
    wn.update()
    p.setx(p.xcor() + p.dx)
    p.sety(p.ycor() + p.dy)

    #bordes
    if p.ycor() > 290:
        p.dy *= -1
    if p.ycor() < -290:
        p.dy *= -1
    #Bordes derecha
    if p.xcor() > 390:
        p.goto(0,0)
        jA.goto(-350,0)
        jB.goto(350,0)
        p.dx = 0.2
        p.dx *= -1
        marA += 1
        pen.clear()
        pen.write(f"JUGADOR A: {marA}     JUGADOR B: {marB}", align="center",font=("Courier", 24))

    #Bordes izquierda
    if p.xcor() < -390:
        p.goto(0,0)
        jA.goto(-350,0)
        jB.goto(350,0)
        p.dx = 0.2
        p.dx *= -1
        marB += 1
        pen.clear()
        pen.write(f"JUGADOR A: {marA}     JUGADOR B: {marB}", align="center",font=("Courier", 24))


    #Choque de las paletas
    if ((p.xcor() > 340 and p.xcor() < 350) 
        and (p.ycor() < jB.ycor() + 50
        and p.ycor() > jB.ycor() - 50)):
        p.dx += 0.2
        p.dx *= -1
        p.dy *= -1
    
    if ((p.xcor() < -340 and p.xcor() > -350) 
        and (p.ycor() < jA.ycor() + 50
        and p.ycor() > jA.ycor() - 50)):
        p.dx += 0.2
        p.dx *= +1
        p.dy *= +1
