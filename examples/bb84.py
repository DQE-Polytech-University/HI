# -*- coding: utf-8 -*-
"""
Created on Sat May  7 13:51:39 2016

@author: Алена
"""
import numpy as np
import math
import random
eva=input('enter the presence of Eve. If Eves no - no. If He is - yes.: ')
q=input('enter the number of qubits:')
if eva=='no':
    #this generator
    basAlisa=np.random.randint(0,2,int(q))
    print('bases Alise:',basAlisa)
    qubits=[]
    n=0
    while n<int(q):
        if basAlisa[n]==0:
            Pol=np.random.choice([0,90])
            if Pol==0:
                qubit=[[1,0],[1/math.sqrt(2),-1/math.sqrt(2)]]
            else:
                qubit=[[0,1],[1/math.sqrt(2),1/math.sqrt(2)]]
        else:
            Pol=np.random.choice([45,135])
            if Pol==45:
                qubit=[[1/math.sqrt(2),1/math.sqrt(2)],[1,0]]
            else:
                qubit=[[-1/math.sqrt(2),1/math.sqrt(2)],[0,1]]
        qubits.append(Pol)
        n=n+1
    print('polarization qubits: ',qubits)
    #this receiver
    basBob=np.random.randint(0,2,int(q))
    print('bases Bob:',basBob)
    i=0
    PolBob=[]
    while i<int(q):
        if (basAlisa[i]==0 and basBob[i]==0) or (basAlisa[i]==1 and basBob[i]==1) :
            a=qubits[i]
            PolBob.append(a)
        elif basAlisa[i]==0 and basBob[i]==1:
            PB1=np.random.choice([45,135])
            PolBob.append(PB1)
        else:
            PB2=np.random.choice([0,90])
            PolBob.append(PB2)
        i=i+1
    print('Bob measured qubits: ',PolBob)
    Keytrack=[]
    z=0
    while z<int(q):
        if basAlisa[z]==basBob[z]:
            Keytrack.append(qubits[z])
        else:
            pass
        z=z+1
    print('key road: ',Keytrack)
    c=len(Keytrack)
    k=0
    key=[]
    while k<c:
        if Keytrack[k]==0 or Keytrack[k]==45:
            key.append(0)
        else:
            key.append(1)
        k=k+1
    print('key: ',key)
else:
    #this generator
    basAlisa=np.random.randint(0,2,int(q))
    print('bases Alise:',basAlisa)
    qubits=[]
    n=0
    while n<int(q):
        if basAlisa[n]==0:
            Pol=np.random.choice([0,90])
            if Pol==0:
                qubit=[[1,0],[1/math.sqrt(2),-1/math.sqrt(2)]]
            else:
                qubit=[[0,1],[1/math.sqrt(2),1/math.sqrt(2)]]
        else:
            Pol=np.random.choice([45,135])
            if Pol==45:
                qubit=[[1/math.sqrt(2),1/math.sqrt(2)],[1,0]]
            else:
                qubit=[[-1/math.sqrt(2),1/math.sqrt(2)],[0,1]]
        qubits.append(Pol)
        n=n+1
    print('polarization Alise: ',qubits)
    #this receiver
    basBob=np.random.randint(0,2,int(q))
    basEva=np.random.randint(0,2,int(q))
    print('bases Bob:',basBob)
    print('bases Eve:',basEva)
    i=0
    PolBob=[]
    while i<int(q):
        if basEva[i]==0 and basBob[i]==0 :
            PB1=np.random.choice([0,90])
            PolBob.append(PB1)
        elif basEva[i]==1 and basBob[i]==1:
            PB2=np.random.choice([45,135])
            PolBob.append(PB2)
        else:
            a=qubits[i]
            PolBob.append(a)
        i=i+1
    print('Polarization of qubits after Eve ',PolBob)
    Keytrack=[]
    z=0
    while z<int(q):
        if basAlisa[z]==basBob[z]:
            Keytrack.append(PolBob[z])
        else:
            pass
        z=z+1
    print('key road: ',Keytrack)
    c=len(Keytrack)
    k=0
    key=[]
    while k<c:
        if Keytrack[k]==0 or Keytrack[k]==45:
            key.append(0)
        else:
            key.append(1)
        k=k+1
    print('key : ',key)
          
    
            
                
