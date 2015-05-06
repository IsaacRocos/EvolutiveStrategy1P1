'''
Created on 05/05/2015

@author: Isaac
'''
import random
import sys
from decimal import *

class Evolutivo1P1(object):

    '''
    Constructor
    '''
    def __init__(self):
        self.sigma = 0.2
        self.exitos = 0
        self.C = 0.817
        self.numVar = 2
        self.mejorSolucion = []
        self.MAX_ITER = 20000
        if len(sys.argv) > 1:
            argumento = sys.argv[1]
            self.numVar = int(argumento)


    def RUN(self):
        print("*****************************")
        print("* ALGORITMO EVOLUTIVO 1 + 1 *")
        print("*****************************")
        print '|NUMERO DE VARIABLES(d):',self.numVar,'| SIGMA:',self.sigma,'| MAX_ITER:',self.MAX_ITER,'|'
        print ""
        print "Generando Primer individuo ... "
        padre = self.generaSecAleatoria(-5,5)
        print "Individuo 0 =",padre
        hijo = []
        #----------------------------------------------------
        print "EJECUTANDO GENERACIONES..."
        for generacion in range(self.MAX_ITER):
            aptPadre = self.aptitud(padre)
            hijo = self.mutar(padre)
            aptHijo = self.aptitud(hijo)
            print '<<G',generacion,'>> ','[PADRE]',aptPadre,padre,' [HIJO]',aptHijo,hijo
            if(aptHijo<aptPadre): # Mejor indivuduo
                padre = hijo[:] # reemplazo padre por hijo
                self.mejorSolucion = []
                self.mejorSolucion.append(generacion)
                self.mejorSolucion.append(aptHijo)
                self.exitos = self.exitos + 1
                print "========================================="
                print '== <<G',generacion,'>>     |MUTACION EXITOSA|'
                print "========================================="
                print ""
            if(generacion!=0 and (generacion%(10*self.numVar))==0):
                print "====|ACTUALIZANDO SIGMA|===="
                self.modificarSigma()
            
        print ""
        print "Proceso finalizado."
        print "---------------------------"
        print "MEJOR INDIVIDUO ENCONTRADO:"
        print '>>[GENERACION]',self.mejorSolucion[0] ,' [APTITUD]',self.mejorSolucion[1],'[GENOMA]',padre 
        print "---------------------------"
        

    def generaSecAleatoria(self,li,ls):
        solucionInic = []
        for i in range(self.numVar):
            solucionInic.append(random.uniform(li,ls))
        return solucionInic
    
    def aptitud(self,individuo):
        # Obtener valor de la derivada de la funcion, si el valor resultante es menor que self.Epsilon, la solucion es valida
        fxsum = 0
        for gen in individuo:
            sxi = ((gen)**4) - (16*(gen)**2) + (5*(gen))
            fxsum = fxsum+sxi
        fx = 0.5 * fxsum
        return fx
    
    def mutar(self,individuo):
        nuevoIndividuo = []
        secuenciaM = []
        #secuenciaM.append(random.uniform(-1,1))
        #secuenciaM.append(random.uniform(-1,1))
        for i in range(self.numVar):
            secuenciaM.append(random.normalvariate(0,1))
        unGen = 0
        for gen in individuo:
            genMut = gen + (self.sigma * secuenciaM[unGen])
            nuevoIndividuo.append(genMut)
            unGen +=1
        return nuevoIndividuo
    
    def modificarSigma(self):
        ps = self.exitos / (10*self.numVar)
        if(ps > 0.2):
            self.sigma = self.sigma / self.C
            print "[ps > 0.2]Sigma actualizada: ", self.sigma
        elif(ps<0.2):
            self.sigma = self.sigma * self.C
            print "[ps < 0.2]Sigma actualizada: ", self.sigma
        elif(ps==0.2):
            print "[ps = 0.2]Sigma se mantiene: ", self.sigma
        self.exitos = 0    
            

chispaVida = Evolutivo1P1()
chispaVida.RUN()
