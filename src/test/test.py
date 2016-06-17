# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 08:35:53 2016

@author: Алена
"""

import unittest
import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from src.Classes import *


class TestClass(unittest.TestCase):
        def test_type(self):
                self.assertEqual(type(long_message), int, 'long_message should be int')
                self.assertEqual(type(number_bas), int, 'number_bas should be int')
                self.assertEqual(type(index_entanglement), int, 'index_entanglement should be int')

        def test_positive(self):
                self.assertGreaterEqual(long_message, 0, 'long_message should be >0')
                self.assertGreaterEqual(number_bas, 0, 'number_bas should be >0')
                self.assertGreaterEqual(index_entanglement, 0, 'index_entanglement should be >0')

        def test_size(self):
                self.assertGreaterEqual(long_message,len(key))

if __name__ == "__main__":
        unittest.main()