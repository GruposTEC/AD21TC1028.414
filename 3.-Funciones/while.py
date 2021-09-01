#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 13:39:27 2021

@author: avmejia
"""

#Uso del while como ciclo infinito y como romperlo
i = 0;
while(True):
    #print(f"El valor de i es : {i}")
    #i = i + 1
    valor = int(input("Dame el número : "))
    if(valor == 0):
        break
print("fuera del break")    

#uso del while si sabemos cuantas veces se va a repetir
i=0
while(i<10):
    print(f"El valor de i es : {i}")
    i = i + 1
    