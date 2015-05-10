'''
Created on 09/05/2015

@author: Isaac
'''
from math import sin, cos
from Evolutivo1P1 import Evolutivo1P1

class SchafferN4(Evolutivo1P1):

    def __init__(self):
        print '***********************************'
        print "|EJECUTANDO (4) SchafferFunctionN4|"
        print '***********************************'
        self.sigma = 0.2
        self.exitos = 0
        self.CExplotar = 0.817
        self.CExplorar = 1.0005
        self.numVar = 2
        self.mejorSolucion = []
        self.MAX_ITER = 10000
        self.interInf = -100
        self.interSup = 100
    
    #@Override
    def aptitud(self,individuo):
        x1 = individuo[0]
        x2 = individuo[1]
        fx = 0.5  +  (cos(sin(abs(x1**2 - x2**2)))  -  0.5) / ( 1 + (0.001*(x1**2 + x2**2)) )**2 
        return fx

funSchafferN4 = SchafferN4()
funSchafferN4.RUN() 
