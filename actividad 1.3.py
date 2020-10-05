#conectarce a alguna db de proteinas y descargas
#a dos proteínas del tipo Mioglobina (Myoglobin) para dos
#especies diferentes (para dos animales distintos)

import urllib.parse
import requests

url = 'http://www.rcsb.org/pdb/rest/search'

queryText = """

<?xml version="1.0" encoding="UTF-8"?>
<orgPdbQuery>

<queryType>org.pdb.query.simple.MoleculeNameQuery</queryType>

<description>Molecule Name Search : Molecule Name=myoglobin</description>

<macromoleculeName>myoglobin</macromoleculeName>

</orgPdbQuery>


"""

print("")
print("querying PDB...\n")

#semantica urllib.request en lugar de urllib2
dataqt = queryText.encode('utf-8')
req = urllib.request.Request(url,data=dataqt)
f = urllib.request.urlopen(req)


result = f.read().decode("utf-8") 

print(result)

if result:
   print(("Found number of PDB entries:", result.count('\n')))
else:
   print("Failed to retrieve results")
