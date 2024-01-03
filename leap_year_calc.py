# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 19:44:30 2023

@author: 16198
"""
year = 2000


if year%4 == 0:
    if year%100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not leap year")
    else:
        print("leap year")
else:
    print("Not leap year")