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
        
        funciones = []
        
        funciones.append(self.funDeJoung)
        funciones.append(self.funRastrigin)
        funciones.append(self.funSchaffer)
        funciones.append(self.funSchafferN4)
        funciones.append(self.funSchwefel)
        funciones.append(self.funMinimizar)
        funciones.append(self.funShubert)
        funciones.append(self.funDeVilliersGlasser)
    
    def runFunc(self):
        print "Ejecutando funciones..."
        for i in range(self.nExec):
            self.funDeJoung.info(i)
            self.funDeJoung.RUN()
        
ejecutar = Ejecutar()
ejecutar.runFunc()

