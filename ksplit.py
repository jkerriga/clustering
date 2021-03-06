from numpy import *
from scipy.stats import kstest
from scipy.cluster.vq import *
from cluster import cluster

def ksplit(data_list,ks_crit):
    
    centroids,labels_init = kmeans2(data_list,2,minit='points')
    count = 1
    labels = labels_init
    cont = ones(1)
    llist = zeros((5000,5000))
    mask = where(llist == 0)
    llist[mask] = -1
    list_list = [2,4,8,16,32,64,128,256,512,1024,2048,2**12]

    l = 0
    for w in range(len(list_list)):
        for k in range(list_list[w]):
            llist[w,k] = l
            l += 1
    j = 0
    p = 2

    # Runs until the sum of cont == 0, when cont > 1 this means that there are still clusters                                      
    # to be clustered                                                                                                         

    while sum(cont) >= 1 :
        cont = zeros(2**count)
        m = 0

        for i in llist[j]:
            # Using the -1 mask on list this allows for the preset cluster #'s to reset.                                                                                                                                                  
            if i == -1:
                break
            # Sets r = positions of ith cluster
            r = data_list[labels_init == i]

            if len(r) == 0:
                continue
            # Feeds the positions of the ith cluster to ks_means which splits the                                                              
            # data into 2 further clusters, then the KS test is used and a p-val                                                               
            # is returned.                                                                                                         
                                                                                                                                
            ks,centroids_,labels = cluster(r)
            
            if ks > ks_crit:
                # This is the condition for a good cluster
                continue
            elif ks == -1:
                break
            else:
                # Re-labels the bifurcated clusters because of non-gaussianity
                a = where(labels_init == i)
                for w in range(2):
                    b = where(labels == w)
                    labels[b] = p
                    p += 1
                    
                centroids = vstack((centroids,centroids_))
                labels_init[a] = labels
                cont[m] = 1
            m += 1

        count += 1
        j += 1

    no_delete = sort(list(set(labels_init)))
    reverse_count = range(max(no_delete)+1)
    for k in reverse_count[::-1]:
        for n in no_delete:
            kill = 1
            if k == n:
                break
            else:
                if kill == len(no_delete):
                    centroids = delete(centroids,k,0)
                kill += 1
                continue
    
    return centroids,labels_init,ks_crit

