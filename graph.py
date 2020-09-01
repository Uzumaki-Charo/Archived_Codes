# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 18:10:33 2019

@author: DELL
"""

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

i=list(x/10 for x in range(11))
j=[1.0,42.209,2385.771,2491.502,2499.78,2499.987,2500.0,2500.0,2500.0,2500.0,2500.0]

#plt.plot(i,j)
fig = plt.figure()
ax = fig.add_subplot(111)

line, = ax.plot(i, j, lw=2)
plt.xticks(np.arange(0, 1, step=0.2))
plt.title('Forest Fire Simulation')
plt.xlabel('Probability of Catching Fire')
plt.ylabel('Number of Burnt Trees')
ax.annotate('Threshold', xy=(0.1, 42.209), xytext=(0.3, 500),
            arrowprops=dict(facecolor='c', shrink=0.0005),
            )

#plt.show()
plt.savefig('graph.png')