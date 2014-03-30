import numpy
from pylab import *
import scipy
##                                                                                                                                                  
# Classification with the assumption of a multivariate gaussian distribution                                                                        
# obs = array of observations x features                                                                                                            
# labels = labels assigned by clustering                                                                                                            
# centroids = average center of clustered observations                                                                                              
# obsToClassify = observations that are added to the observation space and need to be classified                                                    
#                 according to an already existing cluster                                                                                          
##                                                                                                                                                  

def clusterClassification(obs,labels,centroids,obsToClassify):
    SlogLikes = []
    obsLabeled = []
    # for loop runs through each observation being added to observation space                                                                       
    for i in range(shape(obsToClassify)[0]):

        # initialize a very low log like so nested if statement can advance to the next largest value and                                           
        # thus more likely to be in any given cluster                                                                                               
        S = -100000
        #classify = 99999                                                                                                                           
        # runs a specific observation through the likelihood of being in any of the clusters                                                        
        for h in range(max(labels)+1):
            mu = centroids[h,:]
            Z = cov(obs[labels==h].T)
            if shape(Z)[1] == 0:
                continue
            Z = Z + 0.001*rand(shape(Z)[0],shape(Z)[1])
            logLike = -0.5*log(linalg.det(Z)) - 0.5*dot(obsToClassify[i,:]-mu,dot(linalg.inv(Z),obsToClassify[i,:]-mu)) - log(2*pi)
            # if logLike is greater than the prior logLike it means the observation is better suited in the given cluster                           
            if abs(logLike) < abs(S):
                S = logLike
                classify = h

        SlogLikes.append(S)
        obsLabeled.append(classify)

    return SlogLikes,obsLabeled
