# initial skeleton from here: https://matplotlib.org/gallery/lines_bars_and_markers/bar_stacked.html

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


data1 = pd.read_csv("inputdata.csv", ",")

data1 = data1.values

#menMeans = [25, 32, 34, 35, 25]
#womenMeans = [25, 32, 34, 35, 25]
#dogMeans = [25, 32, 34, 35, 25]
#catMeans = [25, 32, 34, 35, 25]

#menMeans = data1["menMeans"].values
#womenMeans = data1["womenMeans"].values
#dogMeans = data1["dogMeans"].values
#catMeans = data1["catMeans"].values

#menMeans.data1[0]
#womenMeans = data1[1]
#dogMeans = data1[2]
#catMeans = data1[3]

menMeans = []
womenMeans = []
dogMeans = []
catMeans = []


for (men, women, dog, cat) in data1:
    menMeans.append(men)
    womenMeans.append(women)
    dogMeans.append(dog)
    catMeans.append(cat)

N = len(menMeans)
print ("N is ", N)

for j in range(1,1):
    for i in range(0, N):
        menMeans.append(menMeans[i])
        womenMeans.append(womenMeans[i])
        dogMeans.append(dogMeans[i])
        catMeans.append(catMeans[i])

N = len(menMeans)

dogBottom = []
catBottom = []

for i in range(0, len(dogMeans)):
    #print ("i is ", i)
    dogBottom.append(menMeans[i] + womenMeans[i])
    catBottom.append(dogBottom[i] + dogMeans[i])

ind = np.arange(N)    # the x locations for the groups
width = 0.9       # the width of the bars: can also be len(x) sequence

plt.figure(figsize=(20,10))

p1 = plt.bar(ind, menMeans, width, zorder=4, color='r')
p2 = plt.bar(ind, womenMeans, width, bottom=menMeans, zorder=3, color='g')
p3 = plt.bar(ind, dogMeans, width, bottom=dogBottom, zorder=2, color='b')
p4 = plt.bar(ind, catMeans, width, bottom=catBottom, zorder=1, color='m')

plt.ylabel('Scores')
plt.title('Scores by group')

#plt.xticks(ind, ('G1', 'G2', 'G3', 'G4', 'G5'))

plt.yticks(np.arange(0, 181, 10))
plt.legend((p1[0], p2[0], p3[0], p4[0]), ('Men', 'Women', 'Dog', 'Cat'))


plt.show()
#plt.savefig('somefigure') # .png
