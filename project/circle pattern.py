import turtle

t = turtle.pen()
t.speed(0)
turtle.bgcolor('black')
colors = ['white', 'red', 'forest green', 'magenta', 'orange',
          'maroon', 'yellow', 'green',
          'cyan', 'indigo', 'dark green', 'violet']
t.penup()
t.goto(0, -100)
t.pendown()
for i in range(80):
    t.pencolor(colors[i % 12])
    for j in range(60):
        t.circle(2.5*j)
