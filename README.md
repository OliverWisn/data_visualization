# Data Visualizations

## Motivation:
I made this data visualizations because I study Data Science. I wanted 
to walk through the Python Standard Library + matplotlib and plotly. 

## Rights:
This data visualizations was made on the basis of the book "Python 
Crash Course - A Hands-On, Project-Based Introduction to Programming" 
by Eric Matthes. The autor of the book give me the right, I quote, "to 
share the code you wrote for the exercises in the book to show people 
what you have learned", but he give me one stipulation, I quote, "as 
long as you're not trying to create a learning resource based largely 
on the material from this book". So please don't create a learning 
resource from this material.

## Requirements: 
python 3.7.9 - rest in requirements.txt .

## Remarks:
- I made this script so that the master branch had always the 
  functioning code.
- The mpl_squares.py script is a standalone script. After running this 
  script, the standard plot of the quadratic function is shown, where 
  the five given points on the plot are connected by straight lines.
- The scatter_squares.py script is a standalone script. After running 
  this script, the plot of the quadratic function is shown, where the 
  points are generated automatically. This script uses the color maps 
  and saves the resulting plot to the file squares_plot.png.
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
- The temperature\death_valley_highs_lows.py script is a standalone 
  script. This script shows death Valley's highest and lowest daytime 
  temperatures in 2018. The area between the data series is shaded. 
  The simple error handling has been added to the script. The plot is 
  also saved by me in the death_valley_highs_lows.png file.

<img src="https://github.com/OliverWisn/data_visualization/blob/master/death_valley_highs_lows.png?raw=true"/>

- The earthquake\eq_world_map.py script is a standalone script. This 
  script displays and saves in an html file in the earthquake 
  directory a world map with marked earthquakes over a period of 30 
  days. The plot is based on the data from the United States 
  Geological Survey downloaded in JSON format.
 
![earthquake](https://user-images.githubusercontent.com/79323713/185978636-9d3c7dd3-0c1c-4ac8-81bc-6db911ff0a34.png)

- The github_repos_visualization\python_repos.py script is 
  a standalone script. The script retrieves data from the GitHub API 
  and prints the information we are interested in in the python shell 
  for the first 30 python repositories that received the highest 
  number of the stars.
- The github_repos_visualization\python_repos_visual.py script is 
  a standalone script. The script retrieves data from the GitHub API 
  and performs a bar visualization for the first 30 python 
  repositories that received the highest number of stars.
  
![python_repos_visual](https://user-images.githubusercontent.com/79323713/185683317-4cab7451-c6ad-446d-97d6-09e0b8579dea.png)

## Data Visualizations Summary:
I had included the following data visualizations in the repository:
- Simple line plot and the scatter plot. 
- Visualization based on series of random decisions (random walk).
- Simulation based on the series of the die rolling with the plotly 
  package, where we checked what will happen when we roll the dice in 
  many different ways. 
- Plot of temperature changes during the day in two places in 
  the USA.
- Visualizing of earthquake data from the JSON file.
- Bar visualization of the data from the GitHub API for the first 30 
  python repositories that received the highest number of stars.

## Version:
- The version of the code only with the simple line plot has tag 1.0.
- The version of the code with the line plot and scatter plot has tag 
  2.0.
- The version of the code with the line plot, scatter plot and random 
  walk has tag 3.0.
- The version 4.0 of the code has the same things as the version 3.0 
  and additionally has the simulation based on the series of the die or 
  dice rolling.
- The version 5.0 of the code has the same things as the version 4.0 
  and additionally has plots of temperature changes during the day in 
  two places in the USA.
- The version 6.0 of the code has the same things as the version 5.0 
  and additionally has plot of the visualizing of the global 
  earthquake data from the JSON file.
- The version 7.0 of the code has the same things as the version 6.0 
  and additionally has plot of the visualizing of the first 30 python 
  repositories from the GitHub API that received the highest number 
  of stars.
