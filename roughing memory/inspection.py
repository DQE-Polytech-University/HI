# -*- coding: utf-8 -*-
"""
Created on Sun May 15 20:49:16 2016

@author: Алена
"""

import numpy as np
import math
from cmath import *

class Qubit:
    def __init__(self,alpha = None,theta = None):
        self.alpha = alfa
        self.theta = theta
        self.qubit =  cos()+sin() 
    
    def __repr__(self):
        return "qubit( " + str(self.alpha)+str(self.theta)+")"
        
    def generate_one_qubit
        


class Generator():
    
    def __init__(self, quantity_bas=None,long_message):
        self.long_message =long_message
        self.quantity_bas = quantity_bas
        
    def write_polarization(self,*args):
        self.write_pol=tuple(args)
        self.len_pol=len(self.write_pol)
        return args
    
    def write_bases(self,*args):
        self.write_bas = tuple(args)
        self.len_bas = len(self.write_bas)
        return args

    def send(self)
        self.__randomly_bases=np.random.choice(self.write_bas,int(self.long_message),True,None)
        self.__randomly_polarization=np.random.choice(self.write_pol,int(self.long_message),True,None)
        
    
    
    
Class Alisa(Generator):
	def __init__(self):
        Generator.__init__(self)
        Generator.send(self)
        
    def get_randomly_bases(self):
        return self.__randomly_bases
        
    def get_randomly_polarization(self):
        return self.__randomly_polarization
        
Class Bob(Generator):
				def __init__(self):
        Generator.__init__(self)
        Generator.send(self)
        
    def get_randomly_bases(self):
        return self.__randomly_bases
        
    def get_randomly_polarization(self):
        return self.__randomly_polarization
        
        
Class Various_measurement():

				def __init__(self):
					q=Generator()
     alica=Alisa()
     boby=Bob()
			  qubit=
    def compare_Bob_Alise(self):
        self.taken_qubits=[]
        i=0
        while i<int(q.long_message):
            if alica.randomly_bases[i]==boby.randomly_bases[i]:
                self.taken_qubits.append(alica.randomly_polarization(i))
            else:
                taken_qubits.append(boby.randomly_polarization(i))
        return self.taken_qubits
        
    def generate_key(self):
        self.key=[]
        i=0
        while i<int(self.set_long):
            if alica.randomly_bases[i]==boby.randomly_bases[i]:
                if (-90)<=self.taken_qubits[i]<90:
                    self.key.append(1)
                else:
                    self.key.append(0)
            else:
                pass
                
                
    
    				
    
    
    
    
    
    