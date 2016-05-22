# -*- coding: utf-8 -*-
"""
Created on Thu May  5 14:50:51 2016

@author: Алена
"""
import numpy as np
import math

class Qubit:
    
    def __init__(self,alpha,theta):
        self.alpha = alpha
        self.theta = theta  
        self.qubit =[[self.alpha, self.theta]]
    
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
        
    def write_theta(self,*args):
        self.write_theta=tuple(args)
        self.len_theta=len(self.write_theta)
        return args
    
    def write_bases(self,*args):
        self.write_bas = tuple(args)
        self.len_bas = len(self.write_bas)
        return args

    def send(self):
        i=0
        self.randomly_theta=[]
        self.randomly_bases=np.random.choice(self.write_bas,self.long_message)
        self.randomly_polarization=np.random.choice(self.write_pol,self.long_message)
        while i<self.long_message:
            const=self.randomly_polarization[i]
            a=0
            while a<self.len_pol:
                if const==self.write_pol[a]:
                    self.randomly_theta.insert(i,self.write_theta[a])
                else:
                    pass
                a=a+1
            i=i+1
        return self.randomly_theta
                    
                

class Alice(Generator):
        
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
        


class Operation_Dice():
    
    def __init__(self,alpha=None,theta=None):
        self.alpha=alpha
        self.theta=theta
        if alpha==None:
            self.alpha=np.random.randint(0,360)
        self.qubit=[[self.alpha,self.theta]]
        if theta==None:
            self.theta=np.random.randint(0,360)
        self.qubit=[[self.alpha,self.theta]]
        
class Various_measurement(Alice,Bob,Generator,Operation_Dice):
    
    def compare_bob_alice(self):
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
            
     def bring_qubits(self):
        self.my_qubits=[]
        n=0
        while n<self.long_message:
            q=Operation_Dice(None,None)
            self.my_qubits.append(q.qubit)
            n=n+1
        return self.my_qubits
        
            
    

    

        
        
        
        
a=Alice(2,10)
a.write_bases(0,1)
a.write_polarization(0,45,33,135)
a.send()
a.get_randomly_polarization()
print(a.she_send_randomly_polarization)
print(a.she_send_randomly_polarization[1])

a=Various_measurement(2,10)
a.bring_qubits()
print(a.my_qubits)

