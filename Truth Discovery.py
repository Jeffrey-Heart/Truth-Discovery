# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import copy
import math
import time

def update_w(A, v_star):
    return np.log(np.sum(np.square(A - v_star))/ np.sum(np.square(A - v_star), axis = 1))

def update_star(A, w):
    return np.sum(A.T*w, axis = 1)/np.sum(w)


def get_loss(A, v_star, w):
    print np.sum(np.sum(np.square((A - v_star)), axis = 1) * w ) 
    return np.sum(np.sum(np.square((A - v_star)), axis = 1) * w )  
        
    

def CRH(A):
    m = 3
    v_star = np.zeros((1, m))
    loss_ = float("inf")
    training_epochs = 100 
    for i in range(training_epochs):
        w = update_w(A, v_star)
        v_star = update_star(A, w)
        loss = get_loss(A, v_star, w)
        if loss<loss_:
            v_ = v_star
            w_ = w
            loss_ = loss
    return v_,w_, loss_


def loadDataset():
    dataset = np.array([[1,2,3],[1.2,2.5,2.5], [0.8,1.9,2.6], [2,4,3.6]])
    return dataset

def loadDataset(fileName):
    with open(fileName) as f:
        lines = f.readlines()
        for line in lines:
            line_list = line.split()
            print line_list

#dataset = loadDataset()
v_, w_, loss_ = CRH(dataset)




    

