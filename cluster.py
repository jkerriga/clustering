#! /usr/bin/env python                                                                                                              

from numpy import *
from scipy.stats import kstest
from scipy.cluster.vq import *
from numpy.random import randn
from numpy.random import rand
from scipy.stats import anderson
import pylab as py
# Define the g-means algorithm                                                                                                     
# This will test the given dataset (r) for gaussianity along the axis                                                              
# that k-means determines is the most important for clustering.                                                                    
# The return value (KS_pval) will be very small (<0.05) if the cluster is nongaussian.                                              #                            will be small if the cluster is gaussian.                                                              

def cluster(r):

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
   
   # Mean subtraction and normalization                                                                                           
   mu = mean(x)
   y = (x-mu)/std(x)

   KS_stat,KS_pval = kstest(y,'norm')
   
   return KS_pval,KS_stat,labels
