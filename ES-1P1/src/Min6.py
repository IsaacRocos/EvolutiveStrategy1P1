'''
Created on 09/05/2015

@author: Isaac
'''
from Evolutivo1P1 import Evolutivo1P1

class Minimizar6(Evolutivo1P1):
    '''
    classdocs
    '''


    def __init__(self):
        print '**********************************'
        print "EJECUTANDO (6) Function6 ..."
        print '**********************************'
        self.sigma = 0.1
        self.exitos = 0
        self.CExplotar = 0.817
        self.CExplorar = 1.1
        self.numVar = 4
        self.mejorSolucion = []
        self.MAX_ITER = 10000
        self.interInf = 0
        self.interSup = 10
        self.m = 10
        self.b = [0.1,0.2,0.2,0.4,0.4,0.6,0.3,0.7,0.5,0.5]
        #B = [1,2,2,4,4,6,3,7,5,5]
        #B = [l*(0.1) for l in B]
        self.c = []
        self.c.append([4.0,1.0,8.0,6.0,3.0,2.0,5.0,8.0,6.0,7.0])
        self.c.append([4.0,1.0,8.0,6.0,7.0,9.0,3.0,1.0,2.0,3.0])
        self.c.append([4.0,1.0,8.0,6.0,3.0,2.0,5.0,8.0,6.0,7.0])
        self.c.append([4.0,1.0,8.0,6.0,7.0,9.0,3.0,1.0,2.0,3.0])
        
        
        #print self.a
    
    #@Override
    def aptitud(self,individuo):
        fxsum = 0
        for i in range(self.m):
            sxj = 0
            for j in range (self.numVar):
                xj = individuo[j]
                cji = self.c[j][i]
                bi = self.b[i]
                sxj +=  (xj - cji)**2 + bi
            fxsum +=  1/sxj
        fx = -1*fxsum
        return fx

funMinimizar = Minimizar6()
funMinimizar.RUN()   
