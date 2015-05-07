'''
Created on 05/05/2015

@author: Isaac
'''
import random
import sys
from decimal import *
from evolutivoPack import Evolutivo1P1

class DeJongF(Evolutivo1P1):

	    def __init__(self):
	    	print "Ejecutando De Joung Function..."
	    	self.setNVar(4)


deJoung = DeJongF()
deJoung.RUN()
