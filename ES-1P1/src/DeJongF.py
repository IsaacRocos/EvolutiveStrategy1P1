'''
Created on 07/05/2015

@author: Isaac
'''
from Evolutivo1P1 import Evolutivo1P1
import sys

class DeJong(Evolutivo1P1):
    '''
    classdocs
    '''

    def __init__(self):
        print "EJECUTANDO (1) DeJoungFunction ..."
        self.sigma = 0.2
        self.exitos = 0
        self.CExplotar = 0.817
        self.CExplorar = 1.01
        self.numVar = 2
        self.mejorSolucion = []
        self.MAX_ITER = 10000
        self.interInf = -65.536
        self.interSup = 65.536
        a1 = [-32,-16,0,16,32]*5
        a2 = [-32]*5 + [-16]*5 + [0]*5 + [16]*5 + [32]*5
        self.a = []
        self.a.append(a1)
        self.a.append(a2)
        print self.a
    
    #@Override
    def aptitud(self,individuo):
        fxsum = 0
        for i in range(24):
            sxi =  1 / ( (i+i) + (individuo[0] - self.a[0][i])**6 + (individuo[1] - self.a[1][i])**6)
            fxsum = fxsum+sxi
        fx = 1 / ( 0.002 + fxsum )
        return fx
    

prueba = DeJong()
prueba.RUN()
