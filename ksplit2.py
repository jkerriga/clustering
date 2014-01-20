
from numpy import *
from pylab import *
from scipy.stats import kstest
from scipy.cluster.vq import *
from cluster import cluster
from scipy.stats.mstats import mode
import matplotlib.pyplot as plt


def ksplit2(data_list,ks_crit):
    
    centroids,labels_init = kmeans2(data_list,2,minit='points')
    p = 0
    l = 2
    
    while p < l+1:
        r = data_list[labels_init == p]        
        ks,centroids,labels = cluster(r)
                
        if ks > ks_crit:
            # This is the condition for a good cluster
            p += 1
            continue
        elif ks == -1:
            break
        else:
            m = where(labels_init == p)
            for i in range(2):
                n = where(labels == i)  
                labels[n[0]] = l
                l += 1
            p += 1
            labels_init[m[0]] = labels    
                
    return centroids,labels_init,ks_crit
        
