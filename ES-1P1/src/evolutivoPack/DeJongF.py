'''
Created on 05/05/2015

@author: Isaac
'''
import random
import sys
from decimal import *
import Evolutivo1P1

class DeJongF(Evolutivo1P1):

	    def __init__(self):
	    	print "Ejecutando De Joung Function..."
	    	self.setNVar(4)

# Obtener valor de la derivada de la funcion, si el valor resultante es menor que self.Epsilon, la solucion es valida
		def aptitud(self,individuo):
			print("***")
			fxsum = 0
	        for gen in individuo:
	            sxi = ((gen)) - (16*(gen)) + (5*(gen))
	            fxsum = fxsum+sxi
	        fx = 0.5 * fxsum
	        return fx

deJoung = DeJongF()
deJoung.RUN()
