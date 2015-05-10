'''
Created on 10/05/2015

@author: Isaac
'''
from math import cos,sin,tanh,exp
from Evolutivo1P1 import Evolutivo1P1

class DeVilliersGlasser(Evolutivo1P1):
    '''
    classdocs
    '''
    def __init__(self):
        
        self.sigma = 0.2
        self.exitos = 0
        self.CExplotar = 1.2
        self.CExplorar = 1.0001
        self.numVar = 5
        self.mejorSolucion = []
        self.MAX_ITER = 10000
        self.interInf = 1
        self.interSup = 60
    
    #@Override
    def aptitud(self,individuo):
        fx1sum = 0
        x1 = individuo[0]
        x2 = individuo[1]
        x3 = individuo[2]
        x4 = individuo[3]
        x5 = individuo[4]
        ti=0
        yi=0
        for i in range(24):
            ti = 0.1*i
            yi = 53.81*(1.27**ti)*tanh(3.012*ti + sin(2.13*ti))*cos(exp(0.507)*ti)
            sx1 = (x1 * (x2**ti) * tanh(x3*ti + sin(x4*ti)) * cos(ti*exp(x5))-yi)**2
            fx1sum = fx1sum+sx1
        fx = fx1sum
        return fx
    
    def info(self,iter):
        if(iter ==0):
            print '******************************************'
            print "|EJECUTANDO (8) DeVilliersGlasserFunction|"
            print '******************************************'
        else:
            print '========== Ejecucion',iter+1,'=========='

    
#funDeVilliersGlasser = DeVilliersGlasser()
#funDeVilliersGlasser.RUN() 
