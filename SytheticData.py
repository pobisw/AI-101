# -*- coding: utf-8 -*-
"""
Created on Wed May 10 21:22:29 2017

@author: pobisw
"""

#import packages
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#create a random dataset with 2 clusters
#cluster1 - mean(-1,0), var(3), both direction
#cluster2 - mean(-5,0), var(2), both direction
dataSet = np.vstack(((np.random.randn(100,2)*3+np.array([-1,0])),
(np.random.randn(75,2)*2+np.array([-5,5]))));


# show data
plt.scatter(dataSet[:,0],dataSet[:,1])
#draw a circle around the cluster

#get the axis
axis = plt.gca();

#add two circles

axis.add_artist(plt.Circle([-1,0],3,fill=False,lw=3));
axis.add_artist(plt.Circle([-5,5],2,fill=False,lw=3));
plt.show();

K = 2;

