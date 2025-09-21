**Reflection Time!**

**Encapsulation:**
A neat part we used encapsulation for was to clean up the beginning of most of our functions.
This was possible through the creation of the jump function.

```
def jump(t: turtle.Turtle, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
```
Instead of entering
```
    t.penup()
    t.goto(x, y)
    t.pendown()
```
at the beginning of each function, we made it possible to use
    ``jump(t, x, y)``
instead.

**Generalization:**
We utilized the process of generalization within our ``draw_jack`` function.
```
def draw_jack(t, x, y, radius):
    draw_pumpkin(t, x, y, radius)
    eye_height = y + .55*2*radius
    mouth_height = y + .3*2*radius
    eye_size = radius / 4
    draw_eye(t, x - (1/3)*radius, eye_height, eye_size)  # Left eye
    draw_eye(t, x + (1/3)*radius, eye_height, eye_size)  # Right eye
    draw_mouth(t, x - (1/3)*radius, mouth_height, radius)  # Mouth
```
We made the eye height, eye size, and mouth height all depend on the x, y, and radius values.
These three values can be changed, so x, y, and radius are more general.
This allowed us to successfully create three separate jack o lanterns with different shapes, sizes, and positions.
