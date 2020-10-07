import actividad13
from Bio import pairwise2
from Bio.pairwise2 import format_alignment

ids = actividad13.get_two_ids_dont_repeat_organism(actividad13.query_molecule_name('myoglobin'))
fasta1 = actividad13.get_fasta_array(ids[0])
fasta2 = actividad13.get_fasta_array(ids[1])

print(fasta1)
print('\n')
print(fasta2)

alignments = pairwise2.align.globalms(fasta1[1], fasta2[1],1,-1,-2,0)
print(type(alignments))
for a in alignments:
    print(format_alignment(*a))


