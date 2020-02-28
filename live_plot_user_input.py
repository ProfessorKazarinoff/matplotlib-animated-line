# live_plot_user_input.py

# import necessary packages
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# intial data
data = [3, 6, 2, 1, 8]

# 
def animate(i):
    with open('data.txt','r') as f:
        for line in f:
            data.append(int(line.strip()))
    plt.cla()

    plt.plot(data[-5:])

# call the animation
ani = FuncAnimation(plt.gcf(), animate, interval=1000)

# show the plot
plt.tight_layout
plt.show()
