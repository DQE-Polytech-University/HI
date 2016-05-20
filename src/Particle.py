# -*- coding: utf-8 -*-
"""
Created on Thu May  5 14:50:51 2016

@author: Алена
"""
import numpy as np
import math

class Qubit:
    
    def __init__(self,alpha=None,theta=None):
        self.alpha = alpha
        self.theta = theta  
        self.qubit = math.cos(alpha)+(math.e**(math.j*theta))*math.sin(alpha)
    
    def __repr__(self):
        return "qubit: " + str(self.qubit)
        



class Generator():
    def __init__(self, quantity_bas,long_message):
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

    def send(self):
        self.randomly_bases=np.random.choice(self.write_bas,self.long_message)
        self.randomly_polarization=np.random.choice(self.write_pol,self.long_message)
        
class Alisa(Generator):
        
    def get_randomly_polarization(self):
        self.she_send_randomly_polarization=self.randomly_polarization
        return self.she_send_randomly_polarization
        
    def get_randomly_bases(self):
        self.she_send_randomly_bases=self.randomly_bases
        return self.she_send_randomly_bases
        
class Bob(Generator):
        
    def get_randomly_polarization(self):
        self.he_send_randomly_polarization=self.randomly_polarization
        return self.he_send_randomly_polarization
        
    def get_randomly_bases(self):
        self.he_send_randomly_bases=self.randomly_bases
        return self.he_send_randomly_bases
        
        
class Various_measurement(Alisa,Bob,Generator):
    
    def compare_Bob_Alise(self):
        self.taken_qubits=[]
        i=0
        while i < self.long_message:
            if self.she_send_randomly_bases[i] == self.he_send_randomly_bases[i]:
                self.taken_qubits.append(self.she_send_randomly_polarization(i))
            else:
                self.taken_qubits.append(self.he_send_randomly_bases(i))
        i=i+1
        return self.taken_qubits
        
    def generate_key(self):
        self.key=[]
        i=0
        while i < self.set_long:
            if self.she_send_randomly_bases[i] == self.he_send_randomly_bases[i]:
                if (-90)<=self.taken_qubits[i]<90:
                    self.key.append(1)
                else:
                    self.key.append(0)
            else:
                pass
    
class Operation_Dice(Qubit):
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
            self.circ = math.e**(turn.imag)
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
            self.circ = math.e**(turn.imag)
            q1 = 0
            q2 = 1
            q3 = self.a
            q4 = (self.circ)*(self.b)
            self.qubit = [[q1,q2],[q3,q4]]
        return self.qubit
        
        
        
        
a=Alisa(2,10)
a.write_bases(0,1)
a.write_polarization(0,45,33,135)
a.send()
a.get_randomly_polarization()
print(a.she_send_randomly_polarization)
print(a.she_send_randomly_polarization[1])

