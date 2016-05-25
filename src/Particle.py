# -*- coding: utf-8 -*-
"""
Created on Thu May  5 14:50:51 2016

@author: Алена
"""
import numpy as np
import math

class Qubit:
    
    def __init__(self,alpha=None,theta=None):
        self.alpha=alpha
        self.theta=theta
        if alpha==None:
            self.alpha=np.random.randint(0,360)
        if theta==None:
            self.theta=np.random.randint(0,360)
        self.qubit=[[self.alpha,self.theta]]
    
    def __repr__(self): #a method for outputting a qubit
        return "qubit: " + str(self.qubit)
        
class Hadamard():
    def __init__(self): 
        self.apply_Hadamard = [[1/math.sqrt(2),1/math.sqrt(2)],[1/math.sqrt(2),-1/math.sqrt(2)]]
    
    def __repr__(self): #a method for outputting a qubit
        return "Hadamard: " + str(self.apply_Hadamard)
        
class NOT():
    def __init__(self):
        self.apply_NOT = [[0,1],[1,0]]
        
    def __repr__(self): 
        return "NOT: " + str(self.apply_NOT)
        
class Phase_gate():
    def __init__(self):
        a = complex(0,1)
        a = a.imag
        self.apply_phase_gate = [[1,0],[0,a]]
        
    def __repr__(self): 
        return "Phase_gate: " + str(self.apply_phase_gate)
        
class Gate_pi():
    def __init__(self):
        p = complex(0,math.pi/4)
        p = p.imag
        self.apply_gate_pi = [[1,0],[0,p]]
        
    def __repr__(self): 
        return "Gate_pi: " + str(self.apply_gate_pi)
        
class CNOT():
    def __init__(self):
        self.apply_CNOT = [[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]]
        
    def __repr__(self): 
        return "Gate_pi: " + str(self.apply_CNOT)



class Actor():
    def __init__(self, quantity_bas,long_message):#This class
    #constructor generator. Set the number of bases used and the message length
        self.long_message =long_message
        self.quantity_bas = quantity_bas
        
    def set_alpha1(self,*args):
    #We set the desired polarization. Example: 0, 45, 90, ...
        self.write_alpha1=tuple(args)
      #  self.len_pol=len(self.write_pol)
        return args
    def set_alpha2(self,*args):
    #We set the desired polarization. Example: 0, 45, 90, ...
        self.write_alpha2=tuple(args)
      #  self.len_pol=len(self.write_pol)
        return args
        
    def write_theta(self,*args):
        #A predetermined angle in the other plane Bloch sphere 
    #to describe the first qubit by appropriate angles
        self.write_theta=tuple(args)
      #  self.len_theta=len(self.write_theta)
        return args
    
    def write_bases(self,*args): 
        #We denote bases for themselves. This agreement
        self.write_bas = tuple(args)
      #  self.len_bas = len(self.write_bas)
        return args

    def send(self):
        #This function is used for a random mixing bases and polarizations.
    #Their use Alice and Bob. But if you need something to mix, call this function.
        i=0
        self.randomly_alpha=[]
        self.randomly_theta=[]
        self.randomly_bases=np.random.choice(self.write_bas,self.long_message)
        while i<self.long_message:
            bas=self.randomly_bases[i]
            a=0
            while a<len(self.write_bas):
                if bas==self.write_bas[a]:
                    self.randomly_alpha.append=np.random.choice([self.write_alpha1[a],self.write_alpha2[a]])
                else:
                    pass
                a=a+1
            i=i+1
        al=0
        while al<self.long_message:
            pol=self.randomly_alpha[al]
            ap=0
            while ap<self.len_pol:
                if const==self.write_pol[a]:
                    self.randomly_theta.insert(i,self.write_theta[a])
                else:
                    pass
                a=a+1
            i=i+1
        return self.randomly_theta
                    
                

class Alice(Generator):#Here they take their randomly values
        
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
        

        
class Various_measurement(Alice,Bob,Generator,Operation_Dice):
    
    def compare_bob_alice(self): #Alice and Bob compare their bases and this
    #forms the following key. If the bases are equal to the true value,
    #if not - then the value of Bob
        self.taken_qubits=[]
        i=0
        while i < self.long_message:
            if self.she_send_randomly_bases[i] == self.he_send_randomly_bases[i]:
                self.taken_qubits.append(self.she_send_randomly_polarization(i))
            else:
                self.taken_qubits.append(self.he_send_randomly_bases(i))
            i=i+1
        return self.taken_qubits
        
        
    def generate_key(self): #generated by the key itself on the trail
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
            
    def bring_qubits(self):#Generates a corresponding qubits. While randomly
        self.my_qubits=[]
        n=0
        while n<self.long_message:
            q=Operation_Dice(None,None)
            self.my_qubits.append(q.qubit)
            n=n+1
        return self.my_qubits
        
class Gate(Qubit):
    
    def transform_qubit(self):#qubit is transformed into a matrix 
    #with the probabilities of its states
        a = math.cos(self.alpha)
        b2 = math.sin(self.alpha)
        b1 = complex(0,self.theta)
        b1 = math.e**(b1.imag)
        b = b1*b2
        self.qubit = [[a],[b]]
        #It Hadamard gates, phase, NOT and pi-gate.
        #They are needed for controlled action on the qubit 
        
        


    

        
        
        
        
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

