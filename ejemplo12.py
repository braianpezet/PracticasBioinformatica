#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Realiza el dot plot para umbral igual a la ventana.
Es decir, si la ventana es de 7 solo colocará un punto 
si hay 7 residuos iguales.

"""

from Bio import SeqIO

#archivo = "ls_orchid.fasta"
#window = 8
archivo = "test3_proteinas.fasta"
window = 8

with open(archivo) as in_handle:
    record_iterator = SeqIO.parse(in_handle, "fasta")
    rec_one = next(record_iterator)
    rec_two = next(record_iterator)



dict_one = {}
dict_two = {}
for (seq, section_dict) in [(str(rec_one.seq).upper(), dict_one),(str(rec_two.seq).upper(), dict_two)]:
    for i in range(len(seq) - window):
        section = seq[i : i + window]
        try:
            section_dict[section].append(i)
        except KeyError:
            section_dict[section] = [i]




# Encuentra las subsecuencias
matches = set(dict_one).intersection(dict_two)
print("%i matches " % len(matches))


# Crea las listas con las coordenadas
x = []
y = []
for section in matches:
    for i in dict_one[section]:
        for j in dict_two[section]:
            x.append(i)
            y.append(j)

import matplotlib.pyplot as plt

fig, ax = plt.subplots()

ax.plot(x, y, '.b')
 
ax.set_xlim(0, len(rec_one) - window)
ax.set_ylim(len(rec_two) - window,0)
#ax.invert_yaxis()
ax.set_xlabel("%s (Longitud %i bp)" % (rec_one.id, len(rec_one)))
ax.set_ylabel("%s (Longitud %i bp)" % (rec_two.id, len(rec_two)))
ax.set_title("Matriz de puntos (window = %i)" % window)

plt.show()

