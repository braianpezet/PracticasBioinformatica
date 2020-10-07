#conectarce a alguna db de proteinas y descargas
#a dos proteínas del tipo Mioglobina (Myoglobin) para dos
#especies diferentes (para dos animales distintos)

from Bio import SeqIO
import urllib
import urllib.parse
import requests
import pypdb
import random
import types

#devulve fasta en un array donde la pos 0 es el encabezado y la pos 1 es la secuencia 
def get_fasta_array(id):
   archivo_fasta_url = "https://www.rcsb.org/fasta/entry/"+id 
   response = urllib.request.urlopen(archivo_fasta_url)
   fasta_sequence = response.read().decode("utf-8", "ignore")
   fasta_sequence = fasta_sequence.split('\n')
   fasta_sequence.pop()
   return (fasta_sequence)

def get_organism(id):
   nombres = list()
   info  = pypdb.get_all_info(id)
   info_nombre = info.get('polymer')
   #esto es porque a veces pueden tener mas de un organismo asociado 
   if(isinstance(info_nombre,list)):
      for x in range (0,len(info_nombre)):
         nombres.append(info.get('polymer')[x].get('Taxonomy').get('@name'))
      return nombres
   return info_nombre.get('Taxonomy').get('@name')

def get_random_id_from_listOfIds(list_of_ids):
   return list_of_ids[random.randint(0,len(list_of_ids)-1)][0:4]

def get_two_ids_dont_repeat_organism(list_of_ids):
   random1 = get_random_id_from_listOfIds(list_of_ids)
   random2 = get_random_id_from_listOfIds(list_of_ids)
   #print (random1)
   #print (random2)
   #print(get_organism(random1))
   #print(get_organism(random2))
   if (get_organism(random1) != get_organism(random2)):
      lista = [random1,random2]
      return lista
   else:
      return get_two_ids_dont_repeat_organism(list_of_ids)
   
def query_molecule_name(name):
   url = 'http://www.rcsb.org/pdb/rest/search'

   queryText = """<?xml version="1.0" encoding="UTF-8"?>

   <orgPdbQuery>

   <version>B0907</version>

   <queryType>org.pdb.query.simple.MoleculeNameQuery</queryType>

   <description>Molecule Name Search : Molecule Name="""+name+"""</description>

   <macromoleculeName>"""+name+"""</macromoleculeName>

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
   

   if result:
      print(("Found number of PDB entries:", result.count('\n')))
   else:
      print("Failed to retrieve results")

   #print(result)
   return result


#ids = get_two_ids_dont_repeat_organism(query_molecule_name('myoglobin'))
#fasta1 = get_fasta_array(ids[0]) 
#fasta2 = get_fasta_array(ids[1])
#print(fasta1)
#print(fasta2)

   #for x in result:
      #print (x[0:4])
      #print(get_organism(x[0:4]))
#response = urllib.request.urlopen(url)
#fasta = response.read().decode("utf-8", "ignore")
#print (fasta)