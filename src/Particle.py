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
        
class Projection_gate():
    
    def __init__(self,*args,**kwargs):
        i=0
        mass_gate1=[]
        mass_gate2=[]
        pol1=args
        pol2=kwargs
        pol=np.random.choice([pol1,pol2])
        while i<len(pol):
            radiany=math.radians(int(pol[i]))
            mass_gate1.append(math.cos(radiany))
            mass_gate2.append(math.sin(radiany))
            i=i+1
        self.gate = [[mass_gate1],[mass_gate2]]
    
    def theta(self,*args):
        thet=args
        mass_gate1=[]
        mass_gate2=[]
        i=0
        while i<len(thet):
            b1 = complex(0,int(thet[i]))
            mass_gate1.append(1)
            mass_gate2.append((math.e**(b1.imag)))
            i=i+1
        self.gate_theta=[[mass_gate1],[mass_gate2]]


class Actor():
    def __init__(self, quantity_bas,long_message):#This class
    #constructor generator. Set the number of bases used and the message length
        self.long_message = long_message
        self.quantity_bas = quantity_bas
        
    def set_alpha1(self,*args):
    #We set the desired polarization. Example: 0, 45, 90, ...
        self.write_alpha1 = args
        return args
        
    def set_alpha2(self,*args):
    #We set the desired polarization. Example: 0, 45, 90, ...
        self.write_alpha2 = args
        return args
        
    def write_theta(self,*args):
        #A predetermined angle in the other plane Bloch sphere 
    #to describe the first qubit by appropriate angles
        self.write_theta = args
        return args
    
    def write_bases(self,*args): 
        #We denote bases for themselves. This agreement
        self.write_bas = args
        return args

    def send(self):
        #This function is used for a random mixing bases and polarizations.
    #Their use Alice and Bob. But if you need something to mix, call this function.
        a=0
        randomly_bases=[]
        self.randomly_alpha=[]
        self.randomly_theta=[]
        i=np.random.choice(int(self.write_bas),self.long_message)
        while a<self.long_message:
            c=[x*0 for x in range(len(self.write_bas))]
            c[i[a]]=1
            randomly_bases.append(c)
        randomly_polarization=[]
        l=0
        while l<self.long_message:
            g=Projection_gate(self.write_alpha1,self.write_alpha2)
            qubit1=np.dot(randomly_bases[l],g.gate)
            pol=math.acos(qubit1[1])
            randomly_polarization.append(math.degrees(pol))
            l=l+1

class Alice(Actor):#Here they take their randomly values
        
    def get_randomly_polarization(self):
        self.she_send_randomly_polarization=self.randomly_polarization
        return self.she_send_randomly_polarization
        
    def get_randomly_bases(self):
        self.she_send_randomly_bases=self.randomly_bases
        return self.she_send_randomly_bases
    
        
class Bob(Actor):
        
    def get_randomly_polarization(self):
        self.he_send_randomly_polarization=self.randomly_polarization
        return self.he_send_randomly_polarization
        
    def get_randomly_bases(self):
        self.he_send_randomly_bases=self.randomly_bases
        return self.he_send_randomly_bases
        

        
class Various_measurement(Alice,Bob,Actor):
    
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
            

        
        
        
        


    

        
        
        


