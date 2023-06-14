#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 11:34:02 2023

@author: yesenia
"""

megas = int(input())

if megas <= 500:
    print(f'Plan #1 - ${megas*2}')
elif megas < 1025:
    print(f'plan #2 - ${megas*1.8}')
elif megas < 2049:
    print(f'plan #3 - ${megas*1.6}')
elif megas < 4097:
    print(f'plan #4 - ${megas*1.4}')
else:
    print(f'plan #5 - ${megas*0.50}')
    