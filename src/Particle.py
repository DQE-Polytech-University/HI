# -*- coding: utf-8 -*-
"""
Created on Thu May  5 14:50:51 2016

@author: Алена
"""
import numpy as np
from math import *

class Particle:
    def __init__(self,bas,n_pol): #selected number of bases and polarizations
        self.set_numberbas=bas #is the number of bases
        self.set_numberpol=n_pol #is the number of polarizations
    def Bas(self): #function shows the number of bases for some reason
        print(self.set_numberbas)
    def formation(self,n_bas): #First you need to enter a selected
    #basis Alice from the array
        a=self.set_numberbas
        if a==1:
            pol=np.random.choice([0,90])
            self.qubit=[[math.cos(pol)][math.sin(pol)]]
        elif a==2:
            if n_bas==0:
                Pol=np.random.choice([0,90])
                if Pol==0:
                    self.qubit=[[1,0],[1/math.sqrt(2),-1/math.sqrt(2)]]
                 #   self.qubit1=[[float(math.cos(Pol/2))][float(math.sin(Pol/2))]]
                else:
                    self.qubit=[[0,1],[1/math.sqrt(2),1/math.sqrt(2)]]
                  #  self.qubit1=[[math.sin(Pol/2)][float(-math.cos(Pol/2))]]
            else:
                Pol=np.random.choice([45,135])
                if Pol==45:
                    self.qubit=[[1/math.sqrt(2),1/math.sqrt(2)],[1,0]]
                  #  self.qubit1=[[math.cos(Pol/2)][-math.sin(Pol/2)]]
                else:
                    self.qubit=[[-1/math.sqrt(2),1/math.sqrt(2)],[0,1]]
                 #   self.qubit1=[[math.sin(Pol/2)][math.cos(Pol/2)]]
        else:
            if n_bas==0:
                pol=np.random.choice([0,90])
                if Pol==0:
                    self.qubit=[[1,0],[1/math.sqrt(2),-1/math.sqrt(2)]]
                else:
                    self.qubit=[[0,1],[1/math.sqrt(2),1/math.sqrt(2)]]
            elif n_bas==1:
                Pol=np.random.choice([45,135])
                if Pol==45:
                    self.qubit=[[1/math.sqrt(2),1/math.sqrt(2)],[1,0]]
                else:
                    self.qubit=[[-1/math.sqrt(2),1/math.sqrt(2)],[0,1]]
            else:
                Pol=np.random.choice([90,-90])
                if Pol==45:
                    self.qubit=[[1/math.sqrt(2),1/math.sqrt(2)],[1,0]]
                else:
                    self.qubit=[[-1/math.sqrt(2),1/math.sqrt(2)],[0,1]]
        print('my qubit',self.qubit)
#q=Particle(2,4)
#q.formation(1)
        def set_the_qubit(self,polariz):
            b=self.set_numberbas
            if b==1:
                self.qub=[[cos(polariz)][sin[polariz]]]
            if b==2:
                if polariz<89:
                    if polariz==0:
                        self.qub=[[1,0],[1/math.sqrt(2),-1/math.sqrt(2)]]
                    else:
                        self.qub=[[1/math.sqrt(2),1/math.sqrt(2)],[1,0]]
                else:
                    if polariz==90:
                       self.qub=[[0,1],[1/math.sqrt(2),1/math.sqrt(2)]]
                    else:
                        self.qub=[[-1/math.sqrt(2),1/math.sqrt(2)],[0,1]]
                
        def teleport(self):
            a1=np.random.choice([0,1])
            if a1==0:
                b1=1
                a2=1
            else:
                b1=0
                a2=0
            if b1==0:
                b2=1
            else:
                b2=0
            self.t_q=[[a1,b2][a2,b1]]
            print('our state:','(','|',a1,'>','|',b2,'>','+','|',a2,'>','|',b1,'>',')','/',sqrt(2))
            self.teleq1=[a1,a2]
            self.teleq2=[b1,b2]
            
            
            

       
