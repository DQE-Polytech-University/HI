# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 07:30:53 2016

@author: Алена
"""

import numpy as np
import math

import Classes as hi

class SARG():
    
    def __init__(self,n,number_bas,long_message,index_entanglement):
        self.the_number_of_inspections = n
        self.long_message = long_message
        self.number_bas = number_bas
        self.index_entanglement = index_entanglement
        
    def run(self):
        i=0
        self.k=0
        while i<self.the_number_of_inspections:
            bb84 = hi.Various_measurement(self.number_bas,self.long_message,self.index_entanglement)
            bb84.begin()
            bb84.compare_bob_alice()
            bb84.generate_key()
            if 4<len(bb84.key):
                self.k=self.k+1
            else:
                pass
            i=i+1
    def request_status(self):
        if self.k == 0:
            print('Eva intervened')
        else:
            print('Eve did not intervene')

a=SARG(6,4,10,0)
a.run()
a.request_status()


