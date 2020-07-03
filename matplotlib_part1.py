from matplotlib import pyplot as plt
import numpy as np


''' Figure 1 : Default Line charts
# Median Developer Salaries by Age
ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]

# Median Python Developer Salaries by Age
py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]

# Median JavaScript Developer Salaries by Age
js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]

plt.plot(ages_x,py_dev_y,color='b', label = 'Python Developers') # marker='o'
# plt.plot(ages_x,py_dev_y,color='#444444', label = 'Python Developers')

plt.plot(ages_x,js_dev_y,color='c', label = 'JS Developers') # marker='o'


#plt.plot(ages_x,dev_y, color='k',linestyle='--',marker='.', label = 'All Developers')
plt.plot(ages_x,dev_y, color='k',linestyle='--', label = 'All Developers')

plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.title("Median Salary(USD) by age")


plt.grid(True)

plt.legend()    # Since we have specified label argument in plt.plot() method, we can just call plt.legend() method directly
# plt.legend(['All Developers','Python Developers'])
plt.tight_layout() # padding for different screen

# plt.style.use('ggplot')
plt.style.use('fivethirtyeight') # fivethirtyeight default colors and grids etc is good.

plt.xkcd
plt.show()
'''



'''Figure 2: Bar Charts'''
ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
# Median All Developer Salaries by Age
dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]

# Median Python Developer Salaries by Age
py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]

# Median JavaScript Developer Salaries by Age
js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]


width = 0.25
x_indexes = np.arange(len(ages_x))



plt.bar(x_indexes - width ,dev_y, width = width, label = 'All Developers')
plt.bar(x_indexes,py_dev_y,width = width, label = 'Python Developers')
plt.bar(x_indexes + width ,js_dev_y,width = width, label = 'JS Developers')


plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.title("Median Salary(USD) by age")

plt.xticks(ticks=x_indexes,labels=ages_x)

plt.legend()
plt.tight_layout()

# plt.style.use('fivethirtyeight')

plt.show()