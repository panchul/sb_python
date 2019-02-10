# initial skeleton from here: https://matplotlib.org/gallery/lines_bars_and_markers/bar_stacked.html

import numpy as np
import matplotlib.pyplot as plt


menMeans = [25, 32, 34, 35, 25]
womenMeans = [25, 32, 34, 35, 25]
dogMeans = [25, 32, 34, 35, 25]
catMeans = [25, 32, 34, 35, 25]

N = len(menMeans)

for j in range(100):
    for i in range(0, N):
        menMeans.append(menMeans[i])
        womenMeans.append(menMeans[i])
        dogMeans.append(menMeans[i])
        catMeans.append(menMeans[i])

N = len(menMeans)

dogBottom = []
catBottom = []

for i in range(0, len(dogMeans)):
    #print ("i is ", i)
    dogBottom.append(menMeans[i] + womenMeans[i])
    catBottom.append(dogBottom[i] + dogMeans[i])

menStd = (2, 3, 4, 1, 2)
womenStd = (3, 5, 2, 3, 3)
dogStd = (3, 5, 2, 3, 3)
catStd = (3, 5, 2, 3, 3)

ind = np.arange(N)    # the x locations for the groups
width = 1.0       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, menMeans, width, zorder=4) # yerr=menStd,)
p2 = plt.bar(ind, womenMeans, width, bottom=menMeans, zorder=3) # , yerr=womenStd
p3 = plt.bar(ind, dogMeans, width, bottom=dogBottom, zorder=2) # , yerr=dogStd
p4 = plt.bar(ind, catMeans, width, bottom=catBottom, zorder=1) # , yerr=dogStd

plt.ylabel('Scores')
plt.title('Scores by group')

#plt.xticks(ind, ('G1', 'G2', 'G3', 'G4', 'G5'))

plt.yticks(np.arange(0, 181, 10))
plt.legend((p1[0], p2[0], p3[0], p4[0]), ('Men', 'Women', 'Dog', 'Cat'))

plt.show()

