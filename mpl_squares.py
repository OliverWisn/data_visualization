import matplotlib.pyplot as plt

# Input values for the x and y axes.
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

# Setting of the chart style.
plt.style.use("Solarize_Light2")

# Generating of the chart.
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

# Defining of the chart title and axis labels.
ax.set_title("Squares of the numbers", fontsize=24)
ax.set_xlabel("Values", fontsize=14)
ax.set_ylabel("Squares of the values", fontsize=14)

# Defining of the size of the labels.
ax.tick_params(axis="both", labelsize=14)

# Chart display.
plt.show()