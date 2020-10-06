#conectarce a alguna db de proteinas y descargas
#a dos proteínas del tipo Mioglobina (Myoglobin) para dos
#especies diferentes (para dos animales distintos)

from Bio import SeqIO
import urllib
import urllib.parse
import requests
import pypdb

#devulve fasta en un array donde la pos 0 es el encabezado y la pos 1 es la secuencia 
def fasta_to_array(archivo_fasta_url):
   response = urllib.request.urlopen(archivo_fasta_url)
   fasta_sequence = response.read().decode("utf-8", "ignore")
   fasta_sequence = fasta_sequence.split('\n')
   return (fasta_sequence)

url = 'http://www.rcsb.org/pdb/rest/search'

queryText = """

<?xml version="1.0" encoding="UTF-8"?>

<orgPdbQuery>

<version>B0907</version>


<queryType>org.pdb.query.simple.MoleculeNameQuery</queryType>

<description>Molecule Name Search : Molecule Name=mCherry</description>

<macromoleculeName>mCherry</macromoleculeName>


</orgPdbQuery>


"""

print("")
print("querying PDB...\n")

#semantica urllib.request en lugar de urllib2
dataqt = queryText.encode('utf-8')
req = urllib.request.Request(url,data=dataqt)
f = urllib.request.urlopen(req)


result = f.read().decode("utf-8") 
result = result.split()
print(result)
print(result[1][0:4]) #para quedarme con un id



if result:
   print(("Found number of PDB entries:", result.count('\n')))
else:
   print("Failed to retrieve results")

url2 = "https://www.rcsb.org/fasta/entry/2C0K"



#response = urllib.request.urlopen(url)
#fasta = response.read().decode("utf-8", "ignore")
#print (fasta)