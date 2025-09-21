import turtle
import math

def polyline(t: turtle.Turtle, n, length, angle):
    for i in range(n):
        t.forward(length)
        t.left(angle)

def arc(t: turtle.Turtle, radius, angle):
    arc_length = 2 * math.pi * radius * angle / 360
    n = 30
    length = arc_length / n
    step_angle = angle / n
    polyline(t, n, length, step_angle)

def jump(t: turtle.Turtle, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def rectangle (t: turtle.Turtle, base, height):
    for length in (base, height, base, height): #1st loop uses base, 2 loop uses height...etc
        t.forward(length)
        t.left(90)

# """ def square(t: turtle.Turtle, length):
   # for i in range(4):
    #    t.forward(length)
     #   t.left(90)

def square(t: turtle.Turtle, length):
    rectangle(t, length, length)

def draw_ribbon(t: turtle.Turtle, x, y, base, height, color="green"):
    jump(t, x, y)
    t.fillcolor(color)
    t.begin_fill()
    rectangle(t, base, height)
    t.end_fill()

def draw_bow(t: turtle.Turtle, x, y, bow_size, color="green"):
    jump(t, x, y)
    temp_color = t.color()
    t.pensize(3)
    t.color(color)
    t.right(15)
    arc(t, bow_size,120)
    t.left(60)
    arc(t, bow_size,120)
    t.right(195)
    arc(t, bow_size,120)
    t.left(60)
    arc(t, bow_size,120)





def draw_present(t:turtle.Turtle, x, y, base, height, ribbon_width, color="red"):
    jump(t, x, y)
    t.fillcolor(color)
    t.begin_fill()
    rectangle(t, base, height)
    t.end_fill()
    p_center = (x + (base / 2))
    r_x = p_center - (ribbon_width / 2)
    draw_ribbon(t, r_x, y, ribbon_width, height)
    r_y = (y + (height / 2)) - (ribbon_width / 2)
    draw_ribbon(t, x, r_y, base, ribbon_width)
    draw_bow(t, p_center, y + height, base / 3)


"""PUT YOUR FUNCTIONS HERE"""

# Create a turtle object
t = turtle.Turtle()

# Hide the turtle and set speed
t.speed(10)  # 1 is slow, 10 is fast, 0 is instant
t.hideturtle()

# Create a window to draw in
# Create a new turtle screen and set its background color
screen = turtle.Screen()
screen.bgcolor("darkblue")
# Set the width and height of the screen
screen.setup(width=600, height=600)
# Clear the screen
t.clear()

t.color("white")
#square(t, 50)
# square(t, 50)
# jump(t, 69, 69)
# square(t, 20)
#rectangle
# rectangle(t, 100, 50)
# jump(t, 69, 69)
# rectangle(t, 50, 100)

# square(t, 50)
# jump(t, 69, 69)
# square(t, 100)

draw_present(t, -10, -50, 69, 69, 5)


"""PUT YOUR DRAW CALLS TO FUNCTIONS HERE"""

# Close the turtle graphics window when clicked
turtle.exitonclick()