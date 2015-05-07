'''
Created on 08/05/2015

@author: Isaac
'''
from Evolutivo1P1 import Evolutivo1P1
import sys
from math import cos, pi as PI

class Rastrigin(Evolutivo1P1):
    '''
    classdocs
    '''

    def __init__(self):
        print "EJECUTANDO (1) RastriginFunction ..."
        self.sigma = 0.2
        self.exitos = 0
        self.CExplotar = 0.817
        self.CExplorar = 1.1
        self.numVar = 4
        self.mejorSolucion = []
        self.MAX_ITER = 100000
        self.interInf = -5.12
        self.interSup = 5.12
    
    #@Override
    def aptitud(self,individuo):
        fxsum = 0
        for i in range(self.numVar):
            xi = individuo[i-1]
            sxi =  (xi**2) - 10*cos(2*PI*xi)
            fxsum = fxsum+sxi
        fx = 10*self.numVar + fxsum
        return fx

prueba = Rastrigin()
prueba.RUN()
