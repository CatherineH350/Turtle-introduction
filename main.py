import turtle
#"turtle" class

count = 0
#turtle.speed(5)
#turtle.pensize(10)
#turtle.shapesize(10,10,10)
#https://cs111.wellesley.edu/content/labs/lab01//images/colorsPage1.png

turtle.shape("turtle")
turtle.color("black")
turtle.fillcolor("pink")
turtle.begin_fill()

for count in range(6):
  turtle.forward(100)
  #turtle.backward(100)
  turtle.right(60) #90 = 90 degrees

turtle.end_fill() 

turtle.penup()
turtle.left(90)
turtle.forward(100)
turtle.pendown()

turtle.fillcolor("coral")
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()

turtle.left(90)
turtle.penup()
turtle.forward(400)
turtle.pendown()

turtle.fillcolor("gold")
turtle.begin_fill()
for i in range(5):
  turtle.forward(100)
  turtle.right(144)
turtle.end_fill()


coolKid = turtle.Turtle()
coolKid.shape("turtle")

coolKid.penup()
coolKid.forward(300)
coolKid.color("black")
coolKid.fillcolor("CadetBlue")
coolKid.begin_fill()
coolKid.pendown()

coolKid.forward(100)
coolKid.left(90)
coolKid.forward(100)
coolKid.left(45)
coolKid.forward(75)
coolKid.left(90)
coolKid.forward(75)
coolKid.left(45)
coolKid.forward(100)

coolKid.end_fill()

coolKid.penup()
coolKid.forward(300)
coolKid.pendown()
coolKid.fillcolor("cornsilk")
coolKid.begin_fill()

for count in range(4):
  coolKid.forward(100)
  coolKid.left(90)

coolKid.end_fill()
coolKid.left(90)
coolKid.forward(100)
coolKid.fillcolor("firebrick")
coolKid.begin_fill()
coolKid.left(90)

for count in range(2):
  coolKid.left(60)
  coolKid.forward(58)
coolKid.left(150)
coolKid.forward(100)

coolKid.end_fill()

coolKid.penup()
coolKid.right(90)
coolKid.forward(100)
coolKid.left(90)
coolKid.backward(75)

coolKid.color("black")
coolKid.fillcolor("DarkSalmon")
coolKid.begin_fill()
coolKid.left(90)
coolKid.forward(40)
coolKid.right(90)
coolKid.forward(20)
coolKid.right(90)
coolKid.forward(40)
coolKid.end_fill()

coolKid.penup()
coolKid.left(90)
coolKid.forward(15)
coolKid.left(90)
coolKid.forward(15)
coolKid.pendown()
coolKid.fillcolor("LightSeaGreen")
coolKid.begin_fill()
coolKid.forward(20)
coolKid.right(90)
coolKid.forward(20)
coolKid.right(90)
coolKid.forward(20)
coolKid.right(90)
coolKid.forward(20)
coolKid.end_fill()


#turtle.forward(100)
#turtle.right(90)
#turtle.forward(100)
#turtle.right(90)
#turtle.forward(100)