#Homework
#1
import turtle
sam = turtle.Turtle()
sam.shape("turtle")
sam.speed('fastest')
#2
def draw_rectangle():
    for i in range(2):
        sam.forward(100)
        sam.left(90)
        sam.forward(25)
        sam.left(90)
# draw_rectangle()
#3
def draw_colour_triangle(colour):
    sam.pencolor(colour)
    for i in range(3):
        sam.forward(100)
        sam.left(120)

# draw_colour_triangle("yellow")

def square(length):
    for i in range(4):
        sam.forward(length)
        sam.left(90)

# square(100)
    
#4
def get_random_colour():
    import random as r
    c = ["red", "orange", "yellow", "green", "blue", "purple"]
    colour = r.choice(c)
    return colour
#5 and 6
# while True:
#     colour = get_random_colour()
#     draw_colour_triangle(colour)
#     sam.left(5)
#     draw_rectangle()

#BONUS
sides = int(input("Whatever shape you want turtle to draw, tell me the amount of sides it has!"))
angle = 360 / sides
colorw = input("What colour do you want your shape to be?")
def draw_shape():
    sam.speed(5)
    sam.fillcolor(colorw)
    sam.begin_fill()
    for i in range(sides):
            sam.forward(100)
            sam.left(angle)
    sam.end_fill()

draw_shape()