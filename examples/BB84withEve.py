# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 07:08:40 2016

@author: Алена
"""
import numpy as np
import math
import Classes as hi

bb84 = hi.Various_measurement(4,10,0)
bb84.begin()
print('Alisa qubits',bb84.qubits_alice)
bb84.intervention()
print('Alisa bases',bb84.she_send_randomly_bases)
print('Eve bases',bb84.eve_creates_bases)
print('Bob bases',bb84.he_send_randomly_bases)
print('Alisa qubits',bb84.qubits_alice)
print('Bob qubits',bb84.qubits_bob)
bb84.compare_bob_alice()
bb84.generate_key()
print(bb84.taken_qubits) 
print(bb84.key)   