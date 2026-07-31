#📈 Matplotlib Basics (Visualization in Python)
#Matplotlib is the most widely used library for data visualization in Python. It helps you create charts, plots, and graphs to understand data visually.

#🔹 1. Why Matplotlib?
#Turns data into visuals (line charts, bar charts, scatter plots, etc.).
#Highly customizable (colors, labels, styles).
# Works seamlessly with NumPy arrays and Pandas DataFrames.

#🔹 2. Basic Plot


import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)          # Line plot
plt.title("Simple Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

#🔹 3. Common Plot Types

import matplotlib.pyplot as plt

# Line Plot
plt.plot([1,2,3],[2,4,6])
plt.show()

# Bar Chart
plt.bar(["A","B","C"], [10,20,15])
plt.show()

# Scatter Plot
plt.scatter([5,7,8],[7,8,6])
plt.show()

# Histogram
plt.hist([1,2,2,3,3,3,4,4,4,4], bins=4)
plt.show()

#🔹 4. Customization

plt.plot(x, y, color="red", linestyle="--", marker="o")
plt.title("Customized Plot")
plt.xlabel("Numbers")
plt.ylabel("Double Value")
plt.grid(True)
plt.show()
#🔹 5. Subplots

fig, axs = plt.subplots(2, 2)

axs[0,0].plot(x, y)
axs[0,0].set_title("Line")

axs[0,1].bar(["A","B","C"], [10,20,15])
axs[0,1].set_title("Bar")

axs[1,0].scatter([5,7,8],[7,8,6])
axs[1,0].set_title("Scatter")

axs[1,1].hist([1,2,2,3,3,3,4,4,4,4], bins=4)
axs[1,1].set_title("Histogram")

plt.tight_layout()
plt.show()

#🎯 Quick Summary
#Matplotlib = Core visualization library in Python.
#Supports line, bar, scatter, histogram, pie charts, and more.
# Highly customizable with labels, colors, styles, and subplots.
# Often used with NumPy & Pandas for data analysis.