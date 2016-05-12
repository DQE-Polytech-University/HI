# -*- coding: utf-8 -*-
"""
Created on Thu May 12 01:52:25 2016

@author: Алена
"""

import numpy as np
import math
from cmath import sin, cos, e

class Particle:
    def __init__(self,bas): #selected number of bases and polarizations
        self.set_numberbas=bas #is the number of bases
        
    def Bas(self): #function shows the number of bases for some reason
        print(self.set_numberbas)
        
    def formation(self,n_bas): #First you need to enter a selected
    #basis Alice from the array
        a=self.set_numberbas
        if a==1:
            self.Pol=np.random.choice([0,90])
            angleinrad=math.radians((int(self.Pol))/2)
            self.qubit=[[math.cos(angleinrad)],[math.sin(angleinrad)]]
        else:
            if n_bas==0:
                self.Pol=np.random.choice([0,90])
                angleinrad=math.radians((int(self.Pol))/2)
                if self.Pol==0:
                    self.qubit=[[1,0],[1/math.sqrt(2),-1/math.sqrt(2)]]
                    self.qubit1=[[math.cos(angleinrad)],[math.sin(angleinrad)]]
                else:
                    self.qubit=[[0,1],[1/math.sqrt(2),1/math.sqrt(2)]]
                    self.qubit1=[[math.sin(angleinrad)],[-math.cos(angleinrad)]]
            else:
                self.Pol=np.random.choice([45,135])
                angleinrad=math.radians((int(self.Pol))/2)
                if self.Pol==45:
                    self.qubit=[[1/math.sqrt(2),1/math.sqrt(2)],[1,0]]
                    self.qubit1=[[math.cos(angleinrad)],[-math.sin(angleinrad)]]
                else:
                    self.qubit=[[-1/math.sqrt(2),1/math.sqrt(2)],[0,1]]
                    self.qubit1=[[math.sin(angleinrad)],[math.cos(angleinrad)]]
class Generator(Particle):        
    def Alisa(self,long_q):
        self.set_long=long_q
        self.basAlisa=np.random.randint(0,2,int(self.set_long))
        self.qubits=[]
        n=0
        while n<int(self.set_long):
            q=Generator(2)
            q.formation(self.basAlisa[n])
            self.qubits.append(q.Pol)
            n=n+1
        print('Alisa bases: ',self.basAlisa)
        print('polarization qubits: ',self.qubits)
    def Bob(self):
        self.basBob=np.random.randint(0,2,int(self.set_long))
        i=0
        self.PolBob=[]
        while i<int(self.set_long):
            if (self.basAlisa[i]==0 and self.basBob[i]==0) or (self.basAlisa[i]==1 and self.basBob[i]==1) :
                a=self.qubits[i]
                self.PolBob.append(a)
            elif self.basAlisa[i]==0 and self.basBob[i]==1:
                PB1=np.random.choice([45,135])
                self.PolBob.append(PB1)
            else:
                PB2=np.random.choice([0,90])
                self.PolBob.append(PB2)
            i=i+1
        print('Bob bases: ',self.basBob)
        print('Bob measured qubits: ',self.PolBob)
        
    def key(self):
        self.Keytrack=[]
        z=0
        while z<int(self.set_long):
            if self.basAlisa[z]==self.basBob[z]:
                self.Keytrack.append(self.qubits[z])
            else:
                pass
            z=z+1
        print('key road: ',self.Keytrack)
        c=len(self.Keytrack)
        k=0
        self.key=[]
        while k<c:
            if self.Keytrack[k]==0 or self.Keytrack[k]==45:
                self.key.append(0)
            else:
                self.key.append(1)
            k=k+1
        print('key: ',self.key)

q1=Generator(2)
q1.Alisa(10)
q1.Bob()
q1.key()