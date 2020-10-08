import actividad13
from Bio import SeqIO

#archivo = "ls_orchid.fasta"
#window = 8

#with open(archivo) as in_handle:
    #record_iterator = SeqIO.parse(in_handle, "fasta")
    #rec_one = next(record_iterator)
    #rec_two = next(record_iterator)
    
#print(rec_one.seq)
#print('------------')
#print(rec_two.seq)
#print(str(rec_one.seq))
#print('Longitud del string: ',len(str(rec_one.seq)))

ids = actividad13.get_two_ids_dont_repeat_organism(actividad13.query_molecule_name('myoglobin'))
fasta1 = actividad13.get_fasta_array(ids[0])
fasta2 = actividad13.get_fasta_array(ids[1])
window = 8

print()
print ('Organismo 1 : ' + actividad13.get_organism(ids[0]))
print ('Fasta')
print(fasta1)
print()
print ('Organismo 2 : ' + actividad13.get_organism(ids[1]))
print ('Fasta')
print(fasta2)

dict_one = {}
dict_two = {}
for (seq, section_dict) in [(str(fasta1[1]).upper(), dict_one),(str(fasta2[1]).upper(), dict_two)]:
    for i in range(len(seq) - window):
        section = seq[i : i + window]
        try:
            section_dict[section].append(i)
        except KeyError:
            section_dict[section] = [i]

matches = set(dict_one).intersection(dict_two)
print("%i matches " % len(matches))

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
 
ax.set_xlim(0, len(fasta1[1]) - window)
ax.set_ylim(len(fasta2[1]) - window,0)
#ax.invert_yaxis()
ax.set_xlabel("%s (Longitud %i bp)" % (fasta1[0], len(fasta1[1])))
ax.set_ylabel("%s (Longitud %i bp)" % (fasta2[0], len(fasta2[1])))
ax.set_title("Matriz de puntos (window = %i)" % window)

plt.show()
