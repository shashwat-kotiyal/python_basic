# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 17:31:53 2020

@author: SKOTIYAL
"""


import os
for root, dirs, files in os.walk(".", topdown=False):
   for name in files:
      print(os.path.join(root, name))
   for name in dirs:
      print(os.path.join(root, name))