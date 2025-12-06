import math
import turtle
import time

def xt(t):
    return 16 * math.sin(t)**3

def yt(t):
    return 13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t)

screen = turtle.Screen()
screen.setup(800, 800)
screen.bgcolor("black")

screen.tracer(0)


heart = turtle.Turtle()
heart.hideturtle()
heart.color("red")
heart.penup()


text = turtle.Turtle()
text.hideturtle()
text.penup()
text.goto(0, -200)

yazi = "Seviliyorsun bebegim"
colors = ["white", "#dddddd", "#bbbbbb", "#999999"]

scale = 10



def kalp_ciz(boyut):
    heart.clear()
    heart.penup()

    for i in range(2550):
        x = xt(i) * boyut
        y = yt(i) * boyut

        if i == 0:
            heart.goto(x, y)
            heart.pendown()
        else:
            heart.goto(x, y)

        
        if i % 10 == 0:
            screen.update()



kalp_ciz(scale)


gosterilen = ""

for harf in yazi:
    gosterilen += harf
    for renk in colors:
        text.clear()
        text.color(renk)
        text.write(gosterilen, align="center", font=("Arial", 22, "bold"))
        screen.update()
        time.sleep(0.03)


while True:
    for s in [scale, scale+1, scale+2, scale+1]:
        kalp_ciz(s)
        screen.update()
        time.sleep(0.08)
