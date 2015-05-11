'''
Created on 10/05/2015

@author: Isaac
'''
from DeJongF import DeJong
from RastriginF import Rastrigin
from SchafferF import Schaffer
from SchafferFN4 import SchafferN4
from SchwefelF import Schwefel
from Min6 import Minimizar6
from ShubertF import Shubert
from DeVilliersGlasser01F import DeVilliersGlasser

class Ejecutar(object):
    
    def __init__(self):
        self.nExec = 10
        self.funDeJoung = DeJong()
        self.funRastrigin = Rastrigin()
        self.funSchaffer = Schaffer()
        self.funSchafferN4 = SchafferN4()
        self.funSchwefel = Schwefel()
        self.funMinimizar = Minimizar6()
        self.funShubert = Shubert()
        self.funDeVilliersGlasser = DeVilliersGlasser()
        
    def runFunc(self, funcion):
        #print "Ejecutando funciones..."
        for i in range(self.nExec):
            print("")
            print '--------------------------------------------------------------------------------------------------------'
            try:
                funcion.info(i)
                funcion.RUN()
            except Exception as ex:
                print "<<ERROR en ejecucion",(i+1),'>>'


ejecutar = Ejecutar()
ejecutar.runFunc(ejecutar.funDeJoung)
print('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')
ejecutar.runFunc(ejecutar.funRastrigin)
print('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')
ejecutar.runFunc(ejecutar.funSchaffer)
print('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')
ejecutar.runFunc(ejecutar.funSchafferN4)
print('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')
ejecutar.runFunc(ejecutar.funSchwefel)
print('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')
ejecutar.runFunc(ejecutar.funMinimizar)
print('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')
ejecutar.runFunc(ejecutar.funShubert)
print('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')
ejecutar.runFunc(ejecutar.funDeVilliersGlasser)
