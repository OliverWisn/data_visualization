# Data Visualizations

## Motivation:
I make this data visualizations because I study Data Science. I would 
like to walk through the Python Standard Library + matplotlib and 
plotly. 

## Rights:
This data visualizations are made on the basis of the book "Python 
Crash Course - A Hands-On, Project-Based Introduction to Programming" 
by Eric Matthes. The autor of the book give me the right, I quote, "to 
share the code you wrote for the exercises in the book to show people 
what you have learned", but he give me one stipulation, I quote, "as 
long as you're not trying to create a learning resource based largely 
on the material from this book". So please don't create a learning 
resource from this material.

## Requirements: 
python 3.10 - rest in requirements.txt .

## Remarks:
- I make this script so that the master branch has always the 
  functioning code.
- The mpl_squares.py script is a standalone script. After running this 
  script, the standard plot of the quadratic function is shown, where 
  the five given points on the plot are connected by straight lines.
- The scatter_squares.py script is a standalone script. After running 
  this script, the plot of the quadratic function is shown, where the 
  points are generated automatically. This script uses the color maps 
  and saves the resulting plot to the file squares_plot.png.

<img src="https://github.com/OliverWisn/data_visualization/blob/master/squares_plot.png?raw=true"/>

- The rw_visual.py script is a standalone script. After running 
  this script, the plot of the random walk is shown, where the 
  points are generated automatically. This script uses the color maps 
  and saves the resulting plot to the file random_walk_plot.png. 
  The first point of the random walk is the big green point on the 
  screen. The last point is the big red point on the screen.

<img src="https://github.com/OliverWisn/data_visualization/blob/master/random_walk_plot.png?raw=true"/>

- The dice\die.py script is a module for the other scripts in 
  the directory.
- The dice\die_visual.py script is a standalone script. When this 
  script is run, the browser shows the frequency graph of the throwing 
  frequency of the one cubic die. The plot is also saved by the script 
  in the d6.html file. It was made into an image called d6_plot.png.
- The dice\dice_visual.py script is a standalone script. When this 
  script is run, the browser shows the frequency graph of the throwing 
  frequency of the two cubic dice. The plot is also saved by the script 
  in the d6_d6.html file. It was made into an image called 
  d6_d6_plot.png.
- The dice\dice_visual_different_sizes.py script is a standalone 
  script. When this script is run, the browser shows the frequency 
  graph of the throwing frequency of the two different dice: the cubic 
  die and the ten-sided die. The plot is also saved by the script in 
  the d6_d10.html file. It was made into an image called 
  d6_d10_plot.png.
- The temperature\sitka_highs.py script is a standalone script. This 
  script shows the highest daytime temperature in Sitka in 2018.
- The temperature\sitka_highs_lows.py script is a standalone script. 
  This script shows Sitka's highest and lowest daytime temperatures in 
  2018. The area between the data series is shaded.

## Data Visualizations Summary:
I made a simple line plot and the scatter plot. After this I made the 
visualization based on series of random decisions (random walk). Then 
I made a simulation based on the series of the die rolling with 
the plotly package, where we checked what will happen when we roll 
the dice in many different ways. The next visualization will be a plot 
of temperature changes during the day in two cities in the USA.

## Version:
- The version of the code only with the simple line plot has tag 1.0.
- The version of the code with the line plot and scatter plot has tag 
  2.0.
- The version of the code with the line plot, scatter plot and random 
  walk has tag 3.0.
- The version 4.0 of the code has the same things as the version 3.0 
  and additionally has the simulation based on the series of the die or 
  dice rolling.