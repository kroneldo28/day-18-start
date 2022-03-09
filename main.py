import turtle
from turtle import Turtle, Screen
from random import choice, randint

turtle.colormode(255)
tim = Turtle()
tim.shape("turtle")
tim.color("purple")
tim.speed(0)


# Let's right a method to draw shapes given the number of sides
def draw_a_shape(sides):
    for i in range(sides):
        tim.forward(100)
        tim.right(360 / sides)


# Let's change color randomly to the turtle
def change_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    # rgb = (r, g, b)
    tim.color(r, g, b)


# Let's define a method that will random change direction to the turtle and change his color
def random_direction():
    directions = [0, 1, 2]
    direction = choice(directions)
    if direction == 1:
        tim.right(90)
        change_color()
    elif direction == 2:
        tim.left(90)
        change_color()
    else:
        change_color()


def draw_spirograph(gap):
    for i in range(int(360/gap)):
        tim.circle(50)
        tim.setheading(tim.heading()+gap)
        change_color()


# # Draw a square
# for i in range (0, 4):
#     tim.forward(100)
#     tim.right(90)

# # Draw a Dashed Line
# for i in range(10):
#     tim.forward(10)
#     tim.pu()
#     tim.forward(10)
#     tim.pd()


# Drawing Different Shapes
# for i in range(3, 11):
#     draw_a_shape(i)
#     change_color()


# # Draw a Random Walk
# tim.pensize(10)
# for _ in range(100):
#     tim.forward(15)
#     random_direction()

# Draw a Spirograph
draw_spirograph(3)


screen = Screen()
screen.exitonclick()
