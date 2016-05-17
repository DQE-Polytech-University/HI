# -*- coding: utf-8 -*-
"""
Created on Sun May 15 20:49:16 2016

@author: Алена
"""

import numpy as np
import math
from cmath import sin, cos, e

class Qubit:
    
    def Polarization(self,*args):
        self.tuple_pol=tuple(args)
        self.len_pol=len(self.tuple_pol)
        return args
        
    def Keyon(self, r):
        self.taken_qubits=r
        self.key=[]
        if (-90)<=self.taken_qubits<90:
            self.key.append(1)
        else:
            self.key.append(0)
        
    
    
q=Qubit()
q.Polarization(0,45,90,135)
q.Keyon(-99)
print(q.key)
