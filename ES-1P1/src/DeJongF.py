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
        self.C = 0.817
        self.numVar = 2
        self.mejorSolucion = []
        self.MAX_ITER = 10000
        self.interInf = -65.536
        self.interSup = 65.536
        
    #@Override
    def aptitud(self,individuo):
        fxsum = 0
        for i in range(25):
            sxi = 
            fxsum = fxsum+sxi
        fx = 1 / ( 0.002 + fxsum )
        return fx
    

prueba = DeJong()
prueba.RUN()

