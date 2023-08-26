import turtle
q = turtle.Turtle()
b = turtle.Turtle()
#q.speed(0)
#b.speed(0)
q.color("#36D1D6")
q.width(3)
b.color("black")
b.width(15)

q.speed(0)
b.speed(0)

wn=turtle.Screen()
wn.bgcolor("black")

#RESETER
q.up()
q.right(90)
q.forward(200)
q.right(-90)
b.up()
b.right(90)
b.forward(200)
b.right(-90)

#Main Circle
q.begin_fill()
q.circle(200)
q.end_fill()

#Sepratators i think 
b.left(60)
b.left(90)
b.up()
b.goto(0,0)

b.down()
b.right(90)
for i in range(6):
    b.right(60)
    b.forward(200)
    b.goto(0,0)

#Resetter 2.0
b.right(60)
b.up()
b.right(90)
b.forward(200)
b.right(-90)

#Triangle I guess

#Blue fill
q.begin_fill()
q.down()
q.left(60)
q.forward(345)
q.left(120)
q.forward(345)
q.left(120)
q.forward(345)
q.end_fill()

#Black OUTLINE
b.down()
b.left(60)
b.forward(345)
b.left(120)
b.forward(345)
b.left(120)
b.forward(345)

#Resseter 3.0
b.left(60)

#Interior triangle with the three thin lines:

#Thin line 1
b.left(90)
b.width(6)
b.forward(100)

#Triangle side 1
b.width(10)
b.right(30)
b.forward(173)

#Thin line 2
b.right(30)
b.width(6)
b.forward(100)
b.left(180)
b.forward(101)

#Triangle side 2
b.width(10)
b.right(30)
b.forward(173)

#Thin line 3
b.right(30)
b.width(6)
b.forward(100)
b.left(180)
b.forward(101)

#Triangle side 3
b.width(10)
b.right(30)
b.forward(173)


#HIDE'S THE TURTLE
b.hideturtle()
q.hideturtle()

#_________________________________________________________________________________________________________________________________________________#

