# -*- coding: utf-8 -*-
"""
Created on Fri May 13 17:13:49 2016

@author: Алена
"""
import numpy as np
import math
from cmath import sin, cos, e

class Qubit:
    
    def __init__(self,polariz=None,circular=None):
        self.alfa = polariz
        self.theta = circular  
    
    def __repr__(self):
        return "qubit: " + str(self.qubit)
        
    def set_the_qubit(self):
        if self.alfa==None and self.theta==None:
            self.set_polariz_for_qubit = np.random.randint([0,380])
            self.circular_pol = np.random.choise([90,-90])
            f = self.circular_pol
            turn = complex(0,f)
            angle = self.set_polariz_for_qubit
            angle_in_rad = math.radians((int(angle))/2)
            self.a = math.cos(angle_in_rad)
            self.b = math.sin(angle_in_rad)
            self.circ = e**(turn.imag)
            q1 = 0
            q2 = 1
            q3 = self.a
            q4 = (self.circ)*(self.b)
            self.qubit = [[q1,q2],[q3,q4]]
        elif self.alfa == 361 and self.theta ==0:
            a1=np.random.choice([0,1])
            if a1==0:
                b1 = 1
                a2 = 1
            else:
                b1 = 0
                a2 = 0
            if b1==0:
                b2 = 1
            else:
                b2 = 0
            self.qubit = [[a1,b2][a2,b1]]
            self.teleq1 = [a1,a2]
            self.teleq2 = [b1,b2]
        else:
            f = self.theta
            turn = complex(0,f)
            angle = self.alfa
            angle_in_rad = math.radians((int(angle))/2)
            self.a = math.cos(angle_in_rad)
            self.b = math.sin(angle_in_rad)
            self.circ = e**(turn.imag)
            q1 = 0
            q2 = 1
            q3 = self.a
            q4 = (self.circ)*(self.b)
            self.qubit = [[q1,q2],[q3,q4]]
            
#q=Qubit(45,0)
#q.set_the_qubit()
#print (q) 
            
class Generator(Qubit):
    
    def Alisa(self, number_bas=None,Long_message):
        self.set_long = Long_message
        self.bas = number_bas
        
    def Polarization(self,*args):
        self.tuple_pol=tuple(args)
        self.len_pol=len(self.tuple_pol)
        return args
    
    def Bases(self,*args):
        self.tuple_bas = tuple(args)
        self.len_bas = len(self.tuple_bas)
        return args 
    
    def Alise_create(self):
        self.bas_Alisa=np.random.choice(self.tuple_bas,int(self.set_long),True,None)
        self.go=np.random.choice(self.tuple_pol,int(self.set_long),True,None)
    
    def Bob_create(self):
        self.Bobi=np.random.choice(self.tuple_pol,int(self.set_long),True,None)
        self.Bob_pol=np.random.choice(self.tuple_pol,int(self.set_long),True,None)
        
    def Bob_measures(self):
        self.taken_qubits=[]
        i=0
        while i<int(self.set_long):
            if self.bas_Alisa[i]==self.bas_Bob[i]:
                self.taken_qubits.append(self.go(i))
            else:
                taken_qubits.append(self.Bob_pol(i))
        return self.taken_qubits
        
    def Key(self):
        self.key=[]
        i=0
        while i<int(self.set_long):
            if self.bas_Alisa[i]==self.bas_Bob[i]:
                if (-90)<=self.taken_qubits[i]<90:
                    self.key.append(1)
                else:
                    self.key.append(0)
            else:
                pass


