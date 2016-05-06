# -*- coding: utf-8 -*-
"""
Created on Thu May  5 14:50:51 2016

@author: Алена
"""
import numpy as np
import math
class Particle:
    def __init__(self,bas,pol):
        self.set_numberbas=bas
        self.set_numberpol=pol
#qubit=Particle(2,4)
#print(qubit.set_numberbas,qubit.set_numberpol)
    def Bas(self):
        print(self.set_numberbas)
        #self.set_bas=n
    def set_Poll(self):
        self.polarization=self.set_numberpol
        self.basis=self.set_numberbas
        if self.polarization==0:
            if self.basis==1:
                a=np.random.randint(0,2)
                b=np.random.randint(0,2)
                self.qubit=[[a],[b]]
                
                
        
      #  i=0
      #  while i<=lenght:
         #   if Alisa[i]==0:
           #     Pol=np.random.choise([0,90])
                

class Generator:
    def __init__(self,lenght,n_bas,n_pol):
        self.lenght_string=lenght
    def rand_bas(self,number,lenght):
       # global lenght
        self.stroka=lenght
        self.Alisa=np.random.randint(0,number,lenght)
#Alisabas=Particle()
#Alisabas.rand_bas(2,10)
#print(Alisabas.stroka,Alisabas.Alisa)