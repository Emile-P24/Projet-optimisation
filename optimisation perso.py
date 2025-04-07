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

# Partie II

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
print("Profit théorique maximal = "+ str(profit(c,v,d,A,alpha)))


# Question 7
d1 = np.array([400,67,33])
d2 = np.array([500,80,53])
d3 = np.array([300,60,43])
p1 = 0.5
p2 = 0.3
p3 = 0.2

def f2(qr): # On minimise l'espérance du profit
    q = qr[:3]
    r = qr[-5:]
    return ( p1*(numpy.dot(c,r) - np.dot(v,np.transpose(h(q,d1,alpha)))) 
            +p2*(numpy.dot(c,r) - np.dot(v,np.transpose(h(q,d2,alpha))))
            +p3*(numpy.dot(c,r) - np.dot(v,np.transpose(h(q,d3,alpha)))))

print(optimize.minimize(f2,np.zeros(8),method='SLSQP', constraints = [{'type':'ineq', 'fun':contrainte1},{'type':'ineq', 'fun':contrainte2}]))


# Partie III
def h_min(q,d): # on remplace h par la fonction min
    h = np.zeros(len(q))
    for i in range(len(q)):
        h[i] = min(q[i],d[i])
    return h

def f3(qr): # Cette fonction ne permet pas de résoudre le problème d'optimisation, car f n'est pas différentiable, on cherche dans la suite à appliquer des nouvelles contraintes pour résoudre ce problème
    q = qr[:3]
    r = qr[-5:]
    return numpy.dot(c,r) - np.dot(v,np.transpose(h_min(q,d)))

# Question 9
def f3(qu):
    q = qu[:3]
    u = [qu[3:6],qu[6:9],qu[9:]]
    cAq = numpy.dot(c,np.dot(A,q))
    return (p1*(cAq - np.dot(v,u[0])) 
            +p2*(cAq - np.dot(v,u[1]))
            +p3*(cAq - np.dot(v,u[2])))

def contrainte3(qu):
    q = qu[:3]
    u = [qu[3:6],qu[6:9],qu[9:12]]
    return q-u[0]
def contrainte4(qu):
    q = qu[:3]
    u = [qu[3:6],qu[6:9],qu[9:12]]
    return q-u[1]
def contrainte5(qu):
    q = qu[:3]
    u = [qu[3:6],qu[6:9],qu[9:12]]
    return q-u[2]
def contrainte6(qu):
    q = qu[:3]
    u = [qu[3:6],qu[6:9],qu[9:12]]
    return d1-u[0]
def contrainte7(qu):
    q = qu[:3]
    u = [qu[3:6],qu[6:9],qu[9:12]]
    return d2-u[1]
def contrainte8(qu):
    q = qu[:3]
    u = [qu[3:6],qu[6:9],qu[9:12]]
    return d3-u[2]
    
print(optimize.minimize(f3,np.zeros(12),method='SLSQP', constraints = [{'type':'ineq', 'fun':contrainte3},
                                                                       {'type':'ineq', 'fun':contrainte4},
                                                                       {'type':'ineq', 'fun':contrainte5},
                                                                       {'type':'ineq', 'fun':contrainte6},
                                                                       {'type':'ineq', 'fun':contrainte7},
                                                                       {'type':'ineq', 'fun':contrainte8}]))