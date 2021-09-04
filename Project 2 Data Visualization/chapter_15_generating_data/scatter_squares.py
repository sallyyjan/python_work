import matplotlib.pyplot as plt
from numpy import sqrt, square

x_values = range(1,1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()

# use colormap
ax.scatter(x_values, y_values, s=10, c=y_values, cmap=plt.cm.Reds)

# set title and axis labels
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# set tick label size
ax.tick_params(axis='both', which='major', labelsize=14)

# set axis range
ax.axis([0, 1100, 0, 1100000])

plt.show()
# or plt.savefig('squares_plot.png', bbox_inches='tight') to auto save as file