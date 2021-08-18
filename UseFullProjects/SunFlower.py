'''Barname baraye namayesh dadan rabete gol aftab gardan ba seri  fibonacci 
baraye Fahm behtar in rabete be https://www.youtube.com/watch?v=_GkxCIW46to sar bezanid'''

# sunflower
# AZ
import turtle as t
pen = t.Turtle()

# settings
pen.speed(0)
pen.pensize(3)

# draw13
n = 13
t = 2
pen.color('blue')
angle = -120
radius = 16
anglePlus = 360 / n
for i in range(n):
    pen.circle(radius, angle, t)
    pen.penup()
    pen.goto(0, 0)
    pen.pendown()
    pen.right(angle + anglePlus)


# draw21
n = 21
t = 4
pen.color('red')
pen.speed(0)
angle = 120
radius = 32
anglePlus = 360 / n
for i in range(n):
    pen.up()
    pen.circle(radius, angle / 3, t)
    pen.down()
    pen.circle(radius, angle / 3 * 2, t)
    pen.penup()
    pen.goto(0, 0)
    pen.pendown()
    pen.right(angle + anglePlus)

# draw34
n = 34
t = 5
pen.color('green')
pen.speed(0)
angle = -120
radius = 64
anglePlus = 360 / n
for i in range(n):
    pen.up()
    pen.circle(radius, angle / 3, t)
    pen.down()
    pen.circle(radius, angle / 3 * 2, t)
    pen.penup()
    pen.goto(0, 0)
    pen.pendown()
    pen.right(angle + anglePlus)

# draw55
n = 55
t = 10
pen.color('purple')
pen.speed(0)
angle = 120
radius = 128
anglePlus = 360 / n
for i in range(n):
    pen.up()
    pen.circle(radius, angle / 3, t)
    pen.down()
    pen.circle(radius, angle / 3 * 2, t)
    pen.penup()
    pen.goto(0, 0)
    pen.pendown()
    pen.right(angle + anglePlus)
