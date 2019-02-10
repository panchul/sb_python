# initially from the tutorials here: https://pythonspot.com/matplotlib-bar-chart/

import matplotlib.pyplot as plt;

plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

objects = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
y_pos = np.arange(len(objects))

performance = [9, 8, 6, 4, 2, 1, 2]
performance2 = [2, 3, 4, 1, 3, 2, 5]



plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.bar(y_pos, performance2, align='center', alpha=0.5)

plt.xticks(y_pos, objects)
plt.ylabel('Here is Y')
plt.title('Here goes the title')

plt.show()
#plt.savefig('somefigure1')
