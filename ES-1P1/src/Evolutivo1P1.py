'''
Created on 05/05/2015

@author: Isaac
'''
import random
import sys

class Evolutivo1P1(object):

    '''
    Constructor
    '''
    def __init__(self):
        self.sigma = 0.1
        self.exitos = 0
        self.C = 0.817
        self.numVar = 2
        self.mejorSolucion = []
        self.MAX_ITER = 10000
        if len(sys.argv) > 1:
            argumento = sys.argv[1]
            self.numVar = int(argumento)


    def RUN(self):
        print("------------------------------------------")
        print("ALGORITMO EVOLUTIVO 1 + 1")
        print("------------------------------------------")
        print '|NUMERO DE VARIABLES(d):',self.numVar,'| SIGMA:',self.sigma,'| MAX_ITER:',self.MAX_ITER,'|'
        print ""
        print "Generando X(0) ... "
        padre = self.generaSecAleatoria(-5,5)
        print "Xo =",padre
        hijo = []
        #----------------------------------------------------
        print "Ejecutando generaciones..."
        for generacion in range(self.MAX_ITER):
            aptPadre = self.aptitud(padre)
            hijo = self.mutar(padre)
            aptHijo = self.aptitud(hijo)
            if(aptHijo<aptPadre): # Mejor indivuduo
                padre = hijo[:] # reemplazo padre por hijo
                self.mejorSolucion = padre[:] # para mantener 
                self.mejorSolucion.append(generacion)
                self.exitos +=1
            if((generacion%(10*self.numVar))==0):
                print("|||Actualizando sigma|||")
                self.modificarSigma()    
            print '<G',generacion,'> ','[P]','<',aptPadre,'> ',padre,' [H]','<',aptHijo,'> ',hijo
        print ""
        print "Proceso finalizado."
        print "---------------------------"
        print "MEJOR SOLUCION ENCONTRADA:"
        print " >> Individuo: ",padre,"en "
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
        secuenciaM.append(random.uniform(-1,1))
        secuenciaM.append(random.uniform(-1,1))
        unGen = 0
        for gen in individuo:
            genMut = gen + (self.sigma * secuenciaM[unGen])
            nuevoIndividuo.append(genMut)
            unGen +=1
        return nuevoIndividuo
    
    def modificarSigma(self):
        ps = self.exitos / (10*self.numVar)
        if(ps > (1/5)):
            self.sigma = self.sigma / self.C
        elif(ps<(1/5)):
            self.sigma = self.sigma * self.C
        self.exitos = 0    
            

chispaVida = Evolutivo1P1()
chispaVida.RUN()
