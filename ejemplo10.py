#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Comparación entre alineamiento algoritmo global y local.

"""
from Bio import pairwise2
from Bio.pairwise2 import format_alignment

##alineamiento global
#for a in pairwise2.align.globalms("ATG", "GGAATGG", 1, -1, -2,0):
    #print(format_alignment(*a))

#alineamiento local, solo da una solución.
for a in pairwise2.align.localms("ATG", "GGAATGG", 1, -1, -2,0):
    print(format_alignment(*a))


