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

def achat (q,A): 
    r = numpy.dot(q,np.transpose(A))
    return r

def h(q,d,alpha):
    h = np.zeros(len(d))
    for i in range(len(d)):
        h[i] = (q[i]*np.exp(-alpha*q[i])+d[i]*np.exp(-alpha*d[i]))/(np.exp(-alpha*q[i])+np.exp(-alpha*d[i]))
    return h

def profit (c,v,d,A,alpha): # profit théorique calculé pour q=d et r = Aq
    return np.dot(v,np.transpose(h(d,d,alpha))) - numpy.dot(c,np.transpose(achat(d,A)))

def f(qr): # qr est la concaténation de q et r, dans cet ordre
    q = qr[:3]
    r = qr[-5:]
    return numpy.dot(c,r) - np.dot(v,np.transpose(h(q,d,alpha)))

def contrainte1(qr): # On veut r > Aq
    q = qr[:3]
    r = qr[-5:]
    return  r - np.dot(A,q)

def contrainte2(qr):# On veut r et q >0
    return qr
    

print(optimize.minimize(f,np.zeros(8),method='SLSQP', constraints = [{'type':'ineq', 'fun':contrainte1},{'type':'ineq', 'fun':contrainte2}]))
print(profit(c,v,d,A,alpha))