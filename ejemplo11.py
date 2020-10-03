#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Alineamiento, visualizar que pueden existir otros locales no tan malos.

"""

from Bio import pairwise2
from Bio.pairwise2 import format_alignment


#alineamiento local, solo da una solución.
for a in pairwise2.align.localms("CAGTATCGT","GTACGTATC", 1, -1, -2,0):
    print(format_alignment(*a))



 
 
