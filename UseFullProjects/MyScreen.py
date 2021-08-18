'''Ye barname baraye screen saver
Ye Eshkal Fni Hst To In Brname Onam Ine Ke Tooye Manitor Haye Ghadimi Vaghti Safhe Bedoon Harkat Roshn Mimoon Baraye Modat Tolani Kharab Mishod In Barname Screen Saver Rng ro Tooye Hmeye Noghat Sfhe Tghiir Mide
Va Baes Mishe Safhe Namayesh Salem Bmoone Vli Tooye In Barname Faghat Ye Ghesmat Az Safhe Rangesh Avaz Mishe'''

# Myscreen
import math as m
import turtle as t
typeWriter = t.Turtle()

# BackGround
t.bgcolor('black')

# TypeWriterSettings


def TypeWriterSet(color):
    typeWriter.goto(-200, -100)
    typeWriter.color(color)
    typeWriter.speed(3)
    typeWriter.pensize(10)


# Draw_AZ
def drawAz():
    typeWriter.pendown()
    # Draw_A
    typeWriter.left(60)
    typeWriter.fd(300)
    typeWriter.left(180 + 60)
    typeWriter.fd(300)
    typeWriter.left(180 + 30)
    typeWriter.penup()
    typeWriter.fd(300 / 2 * m.sqrt(3))
    typeWriter.pendown()
    typeWriter.left(180 + 30)
    typeWriter.fd(150)
    typeWriter.penup()
    typeWriter.fd(99)
    typeWriter.pendown()
    # Draw_Z
    typeWriter.fd(75)
    typeWriter.left(180 + 60)
    typeWriter.fd(150)
    typeWriter.left(90 + 30)
    typeWriter.fd(75)
    typeWriter.penup()


while(True):
    TypeWriterSet('white')
    drawAz()

    TypeWriterSet('red')
    drawAz()

    TypeWriterSet('orange')
    drawAz()

    TypeWriterSet('yellow')
    drawAz()

    TypeWriterSet('green')
    drawAz()

    TypeWriterSet('blue')
    drawAz()

    TypeWriterSet('purple')
    drawAz()
