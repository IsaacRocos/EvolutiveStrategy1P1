'''
Created on 10/05/2015

@author: Isaac
'''
from math import cos
from Evolutivo1P1 import Evolutivo1P1

class Shubert(Evolutivo1P1):
    '''
    classdocs
    '''

    def __init__(self):
        print '***********************************'
        print "|EJECUTANDO (7) ShubertFunction|"
        print '***********************************'
        self.sigma = 0.2
        self.exitos = 0
        self.CExplotar = 0.817
        self.CExplorar = 1.01
        self.numVar = 2
        self.mejorSolucion = []
        self.MAX_ITER = 10000
        self.interInf = -10
        self.interSup = 10
    
    #@Override
    def aptitud(self,individuo):
        fx1sum = 0
        fx2sum = 0
        x1 = individuo[0]
        x2 = individuo[1]
        for i in range(5):
            sx1 = (i+1) * cos((i+1+1)*x1 + (i+1))
            sx2 = (i+1) * cos((i+1+1)*x2 + (i+1))
            fx1sum = fx1sum+sx1
            fx2sum = fx2sum+sx2
            
        fx = fx1sum * fx2sum
        return fx

funShubert = Shubert()
funShubert.RUN() 