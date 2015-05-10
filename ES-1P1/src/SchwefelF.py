'''
Created on 09/05/2015

@author: Isaac
'''
from math import sqrt, sin
from Evolutivo1P1 import Evolutivo1P1

class Schwefel(Evolutivo1P1):

    def __init__(self):
        print '***********************************'
        print "|EJECUTANDO (5) SchafferFunctionN4|"
        print '***********************************'
        self.sigma = 0.2
        self.exitos = 0
        self.CExplotar = 0.817
        self.CExplorar = 1.0001
        self.numVar = 4
        self.mejorSolucion = []
        self.MAX_ITER = 10000
        self.interInf = -500
        self.interSup = 500
    
    #@Override
    def aptitud(self,individuo):
        fxsum = 0
        for i in range(self.numVar):
            xi = individuo[i]
            sxi =  xi * sin(sqrt(abs(xi))) 
            fxsum = fxsum+sxi
        fx = 418.9829*self.numVar - fxsum 
        return fx

funSchwefel = Schwefel()
funSchwefel.RUN() 
