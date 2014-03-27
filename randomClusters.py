from numpy import *
import sys
from numpy.random import randn
from numpy.random import rand
from pylab import *


def randomClusters(number,size1,size2,background):
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
            x_coord = 10*rand()*i*(randx[i]-0.5)
            y_coord = 10*rand()*i*(randy[i]-0.5)
            x_dim = 2*randn(size1)+ x_coord
            y_dim = 2*randn(size1)+ y_coord
            x = append(x,x_dim)
            y = append(y,y_dim)
            x_coordinates = append(x_coordinates,x_coord)
            y_coordinates = append(y_coordinates,y_coord)
            cls_labels = append(cls_labels,ones(size1)*i)
    else:
        sizes = linspace(size1,size2,number)

        for i in range(number):
            x_coord = 25*rand()*i*(randx[i]-0.5)
            y_coord = 25*rand()*i*(randy[i]-0.5)
            x_dim = 0.3*(i+1)*randn(round(sizes[i]))+ x_coord
            y_dim = 0.3*(i+1)*randn(round(sizes[i]))+ y_coord
            x = append(x,x_dim)
            y = append(y,y_dim)
            x_coordinates = append(x_coordinates,x_coord)
            y_coordinates = append(y_coordinates,y_coord)
            cls_labels = append(cls_labels,ones(sizes[i])*i)
    data_list = []
    if background == 'off':
        print "Background noise off."
    else:
        back_x = 20*number*rand(200)-75
        back_y = 20*number*rand(200)-75
        x = append(x,back_x)
        y = append(y,back_y)

    for m in range(len(x)):
        data = array([x[m],y[m]])
        data_list.append(data)
    data_list = vstack(data_list)
    return data_list,x_coordinates,y_coordinates,cls_labels
