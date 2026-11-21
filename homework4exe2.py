import matplotlib.pyplot as plt
import numpy as np

data_x = np.linspace(-10, 10, 21)
data_y = data_x**2

fig, ax = plt.subplots(1,1)
ax.plot(data_x, data_y,
        linewidth=1, color=(0.2, 0, 1), linestyle='-',
        marker='o', markersize=6, markerfacecolor='red',
        markeredgewidth=0.5)
plt.show()

data1_x = np.linspace(0, 4*np.pi, 100)
data1_y = np.sin(data1_x)
data1_y2= np.cos(data1_x)

fig, ax = plt.subplots(1,1)
ax.plot(data1_x, data1_y, label='sin', color='red',
        linestyle='dashed', linewidth=2)
ax.plot(data1_x, data1_y2, label='cos', color='blue')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Sin and Cos')
ax.legend()
plt.show()