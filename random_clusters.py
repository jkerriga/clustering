from numpy import *
from scipy.stats import kstest
from scipy.cluster.vq import *
import sys
from numpy.random import randn
from numpy.random import rand
from ksmeans import ksmeans
from pylab import *
from scipy.stats import anderson


def random_clusters(number,size1,size2):
    x = []
    y = []
    x_coordinates = []
    y_coordinates = []
    randx = rand(number)
    randy = rand(number)
    cls_labels = []
    if size1 == size2:
        sizes = ones(number)*size1
        for i in range(number):
            x_coord = 8*rand()*i*(randx[i]-0.5)
            y_coord = 8*rand()*i*(randy[i]-0.5)
            x_dim = rand()*randn(size1)+ x_coord
            y_dim = rand()*randn(size1)+ y_coord
            x = append(x,x_dim)
            y = append(y,y_dim)
            x_coordinates = append(x_coordinates,x_coord)
            y_coordinates = append(y_coordinates,y_coord)
            cls_labels = append(cls_labels,ones(size1)*i)
    else:
        sizes = linspace(size1,size2,number)

        for i in range(number):
            x_coord = 8*(randx[i]-0.5)*i
            y_coord = 8*(randy[i]-0.5)*i
            x_dim = rand()*(i+1)*randn(round(sizes[i]))+ x_coord
            y_dim = rand()*(i+1)*randn(round(sizes[i]))+ y_coord
            x = append(x,x_dim)
            y = append(y,y_dim)
            x_coordinates = append(x_coordinates,x_coord)
            y_coordinates = append(y_coordinates,y_coord)
            cls_labels = append(cls_labels,ones(sizes[i])*i)
    data_list = []

    for m in range(len(x)):
        data = array([x[m],y[m]])
        data_list.append(data)
    data_list = vstack(data_list)
    return data_list,x_coordinates,y_coordinates,cls_labels
