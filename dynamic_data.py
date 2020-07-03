from matplotlib.animation import FuncAnimation
from itertools import count
import random
import matplotlib.pyplot as plt
import pandas as pd

x_vals = [0, 1, 2, 3, 4, 5]
y_vals = [0, 1, 3, 2, 3, 5]

x_vals=[]
y_vals=[]

# plt.plot(x_vals, y_vals)


index = count()

def animate(i):
    # x_vals.append(next(index))
    # y_vals.append(random.randint(0, 5))
    data = pd.read_csv('data.csv')
    x=data['x_value']
    y=data['total_1']
    y2=data['total_2']
    plt.cla()
    plt.plot(x,y)

ani = FuncAnimation(plt.gcf(),animate,1000)   # time is in milliseconds

plt.tight_layout()
plt.show()


# data = pd.read_csv('data.csv')
# x = data['x_value']
# y1 = data['total_1']
# y2 = data['total_2']