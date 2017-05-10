# -*- coding: utf-8 -*-
"""
Created on Mon May  8 18:35:29 2017

@author: pobisw
"""



import numpy as np
import matplotlib.pyplot as plt

#Implement K means clustering algorithm

# get the intial k centroids which are random points
def initialize_centroids(dataset, K):
    n = len(dataset);
    randK = np.random.randint(low=n,size=[K]);
    return dataset[randK,:];



def get_kmeans_clusters(dataset, K):
    centroids = initialize_centroids(dataset, K);
    plt.scatter(dataset[:,0],dataset[:,1],c='g',s=100);
    plt.scatter(initial_centroids[:,0],intial_centroids[:,1],c='g',s=100);
    max_step = 100;
    threshold = 0.001;
    step = 0;
    old_
    while true:
        step += step;
        old_centroids = centroids;
        label = get_label(centroids, dataset);
        centroids = get_centroids(dataset,label);
        if step > maxstep or np.sqrt((old_centroids-new_centroids)**2).sum())<threshold:
            break;
    
    

def get_label(centroids, datset):
    #calculate the the distnce between each point and centroids
    #label a point as same as the cluster which has smallest distance from
    #this point
     n = len(dataset)
     label = numpy.zeros(n,1);
        
        
def get_centroids(dataset, label, k):
    
    
    