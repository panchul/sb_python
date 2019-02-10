# initially from the tutorials here: https://pythonspot.com/matplotlib-bar-chart/

import numpy as np
import matplotlib.pyplot as plt

# data to plot
n_groups = 4
means_mon = (90, 55, 40, 65)
means_tue = (85, 62, 54, 20)
means_wed = (20, 15, 10, 5)
means_thu = (10, 25, 20, 25)

# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.15
opacity = 1.0

rectsMon = plt.bar(index, means_mon, bar_width, alpha=opacity, color='b', label='mon', zorder=3)
rectsTue = plt.bar(index + bar_width, means_tue, bar_width, alpha=opacity, color='g', label='tue', zorder=2)
rectsWed = plt.bar(index + bar_width, means_wed, bar_width, alpha=opacity, color='y', label='tue', zorder=1)
rectsThu = plt.bar(index + bar_width, means_thu, bar_width, alpha=opacity, color='m', label='tue', zorder=0)



plt.xlabel('here is x label')
plt.ylabel('this is y label')
plt.title('here goes title')
plt.xticks(index + bar_width, ('A', 'B', 'C', 'D'))
plt.legend()

plt.tight_layout()
plt.show()