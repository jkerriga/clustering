
from numpy import *
from pylab import *
from scipy.cluster.vq import *
from gaussianClusterTest import gaussianClusterTest
import matplotlib.pyplot as plt


def gSplit(data_list):
    
    centroids,labels_init = kmeans2(data_list,2,minit='points')
    ## p is keeping track of number to be tested
    p = 0
    ## l is keeping track of those that are to be gaussian tested
    l = 2
    
    while p < l+1:
        ## takes the input observations and splits them between the two clusters (0 or 1)
        ## so each one can be individually tested for gaussianity
        r = data_list[labels_init == p]        
        ad_list = []
        labels_matrix = zeros((len(r),100))
        
        ad,ad_crit,labels = gaussianClusterTest(r)
        # ad < ad_crit means that the null hypothesis cannot be rejected
        # in this case that the cluster is possibly gaussian
        if ad < ad_crit:
            # This is the condition for a good cluster
            p += 1
            continue
        # error condition
        elif ad == -1:
            break
        else:
            # masks the specific obervations that will be re-indexed to new updated
            # cluster numbers
            m = where(labels_init == p)
            for i in range(2):
                n = where(labels == i)  
                labels[n[0]] = int64(l)
                l += 1
            p += 1
            labels_init[m[0]] = int64(labels)    
                
    return centroids,labels_init,ad_crit
        
