import numpy as np
from scipy import optimize
from casadi import *
import time

alpha = 0.1
c = 0.001*np.array([30,1,1.3,4,1])
v = np.array([0.9,1.5,1.1])
d = np.array([400,67,33])
A = np.array([[3.5,2,1],
              [250,80,25],
              [0,8,3],
              [0,40,10],
              [0,8.5,0]])

def achat(d,A): # on veut q = d pour ne pas avoir d'invendus
    r = numpy.dot(d,np.transpose(A))
    return r

def h(q,d,alpha):
    h = np.zeros(len(d))
    for i in range(len(d)):
        h[i] = (q[i]*np.exp(-alpha*q[i])+d[i]*np.exp(-alpha*d[i]))/(np.exp(-alpha*q[i])+np.exp(-alpha*d[i]))
    return h

def profit (c,v,d,A,alpha):
    return np.dot(v,np.transpose(h(d,d,alpha))) - numpy.dot(c,np.transpose(achat(d,A)))

for i in [0.01,1,10,100,1000,100000]:
    print(profit(c,v,d,A,i))