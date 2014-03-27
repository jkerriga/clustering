#! /usr/bin/env python                                                                                                              

from numpy import *
from scipy.stats import kstest
from scipy.cluster.vq import *
from numpy.random import randn
from scipy.stats import anderson

# Define the g-means algorithm                                                                                                     
# This will test the given dataset (r) for gaussianity along the axis                                                              
# that k-means determines is the most important for clustering.                                                                    
# The return value (AD_stat) will be large if the cluster is nongaussian.                                                    
#                           will be small if the cluster is gaussian.                                                              

def gaussianClusterTest(r):

   d,n = shape(r)
   # If the dataset is only one point, return a large number to                                                                       
   # indicate that we have over-fit this cluster                                                                                    
   if d<=1:
       return -1,0,0

   # Run k-means with k=2                                                                                                           
   c=2
   centroids,labels = kmeans2(r,c,minit='points')
   # Find the axis along which the two centroids lie                                                                               
   v = centroids[1,:] - centroids[0,:]
   # Get the projection of each point in r along v                                                                                 
   x = empty((n))
   
   x = dot(r,v)/linalg.norm(v)

   AD_stat,AD_criticals,AD_percent = anderson(x,'norm')   
   # This is the 5% significance level
   AD_crit = AD_criticals[2]

   return AD_stat,AD_crit,labels
