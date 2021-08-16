#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 13:25:09 2021

@author: avmejia
"""

if (False):
    print("dentro del if")
    print("segunda instruccion")
elif (5 > 0):
    print("dentro del elif")
else:
    print("dentro del else")

print("fuera de la decision")

if(False):
    print("dentro del if")
    print("segunda instruccion")
else:
    if (5 > 0):
        print("dentro del elif")
    else:
        print("dentro del else")

print("fuera de la decision")
