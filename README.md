# Random-Walk-Mobility-Model-Using-Turtle-And-Matplotlib
Random Walk is a part of Indoor Mobility Models. Mobile Node moves from current location to a new location by randomly choosing a direction and speed because it is dynamic. It catches the attribute of minimum speed or maximum speed and direction from 0 to 2pi i.e.,, 360 degree. A constant time interval ‘t’ and distance ‘d’.

This Python script generates a visualization of a 2-D random walk mobility model using the turtle graphics library and a bar chart using the Matplotlib library.

The visualization shows an arrow moving in a random direction for a certain number of steps. The arrow's movements are tracked to count the number of times it moves in each of the four directions (north, south, east, and west). The bar chart shows the counts for each direction.

The turtle graphics library is used to draw the x- and y-axes and label them with coordinates. It is also used to draw the arrow and move it in a random direction. The Matplotlib library is used to create the bar chart.

The script begins by importing the necessary libraries (turtle, random, and matplotlib.pyplot) and setting up the screen and axes for the turtle graphics visualization. It then creates a turtle object for the arrow and sets its attributes. The step size and number of steps are also defined.

The script then uses a for loop to randomly choose a direction and move the arrow accordingly for each step. The counts for each direction are tracked in a dictionary.

After the random walk is complete, the turtle graphics visualization is exited, and a bar chart is created using the Matplotlib library. The counts dictionary is used to create a bar chart with the direction on the x-axis and the count on the y-axis.

Overall, this script provides a simple example of a random walk mobility model and demonstrates how to use the turtle graphics and Matplotlib libraries to visualize the model.
