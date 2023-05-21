import turtle
import random
import matplotlib.pyplot as plt

# Set up the screen
screen = turtle.Screen()
screen.bgcolor('white')
screen.title('Random Walk Mobility Model')

# Set up the axes
axes = turtle.Turtle()
axes.hideturtle()
axes.penup()
axes.goto(-250, 0)
axes.pendown()
axes.goto(250, 0)
axes.write('X', font=('Arial', 12, 'normal'))
axes.penup()
axes.goto(0, -250)
axes.pendown()
axes.goto(0, 250)
axes.write('Y', font=('Arial', 12, 'normal'))


# Label the x-axis coordinates
for x in range(-200, 201, 50):
    axes.penup()
    axes.goto(x, -10)
    axes.pendown()
    axes.write(str(x), font=('Arial', 10, 'normal'))

# Label the y-axis coordinates
for y in range(-200, 201, 50):
    axes.penup()
    axes.goto(-10, y)
    axes.pendown()
    axes.write(str(y), font=('Arial', 10, 'normal'))


# Set up the arrow
arrow = turtle.Turtle()
arrow.hideturtle()
arrow.speed(10)
arrow.penup()
arrow.goto(0, 0)
arrow.pendown()
arrow.pensize(2)
arrow.color('red')
arrow.shape('arrow')

# Set up the step size and number of steps
step_size = 20
num_steps = 100

# Count the number of times the arrow moves in each direction
counts = {'north': 0, 'south': 0, 'east': 0, 'west': 0}
for i in range(num_steps):
    # Choose a random direction
    direction = random.choice(['north', 'south', 'east', 'west'])

    # Move the arrow
    if direction == 'north':
        arrow.setheading(90)
        arrow.forward(step_size)
        counts['north'] += 1
    elif direction == 'south':
        arrow.setheading(270)
        arrow.forward(step_size)
        counts['south'] += 1
    elif direction == 'east':
        arrow.setheading(0)
        arrow.forward(step_size)
        counts['east'] += 1
    elif direction == 'west':
        arrow.setheading(180)
        arrow.forward(step_size)
        counts['west'] += 1

# Exit turtle graphics
#turtle.bye()

# Create a bar chart of the counts
fig, ax = plt.subplots()
ax.bar(counts.keys(), counts.values())
ax.set_xlabel('Direction')
ax.set_ylabel('Count')
ax.set_title('Random Walk Bar Chart')
plt.show()
