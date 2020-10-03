#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Ejemplos de alineamiento algoritmo de 

"""
from Bio import pairwise2
from Bio.pairwise2 import format_alignment
#force_generic=True, fuerza a  que use el algoritmo de Needle-Wunsch
for a in pairwise2.align.globalms("GTACGTATC","GTCCTAC",1,-1,-2,0,force_generic=True):
    print(format_alignment(*a))
