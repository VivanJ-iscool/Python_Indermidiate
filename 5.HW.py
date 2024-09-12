#Homework
colors = ["red", "orange", "yellow", "green", "blue", "cyan", "purple", "pink", "magenta", "light green", "light blue"]
import turtle
sam = turtle.Turtle()
sam.shape("turtle")
steps = 48
degrees = 230
import random as r
while True:
    random_color = "red"
    sam.forward(steps)
    sam.left(degrees)
    sam.color(r.sample(colors, 1))