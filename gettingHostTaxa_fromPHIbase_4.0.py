############################################################################################
###   Getting information from PHI-base version 4.0:     ###
####################################################################################################
###   Getting host taxa information from flat-file ("phiBase_version4.0.txt") downloaded         ###
###   directly from PHI-base and then accessing Entrez database to define a host taxonomy name   ###      
####################################################################################################
import sys
from Bio import Entrez
Entrez.email="elzbieta.janowska-sejda@rothamsted.ac.uk"
fileName=("phiBase_version4.0.txt")
outfile = ("phiBase_version4.0_content.txt")
fh1=open(fileName, "r")
fhOut = open (outfile, "w")

taxaDict=dict()
idRow=0    
for line in fh1.readlines():
	line = str(line).strip('\n')
	line = line.split('\t')
    	print "Processing row nb %d" % idRow	
	l= list(line)
    	taxaId = line[11].strip()
    	if taxaDict.has_key(taxaId):
        	records = taxaDict[taxaId]
    	else:
        	handle = Entrez.efetch(db="Taxonomy", id= taxaId, retmode="xml")
        	records= Entrez.read(handle)
    	if ("Metazoa" in records[0]["Lineage"].split("; ")):
        	l.append("Animal Pathogen")          
    	elif ("Viridiplantae" in records[0]["Lineage"].split("; ")):
        	l.append("Plant Pathogen")    
    	else:
        	l.append("Other Pathogen")
    	fhOut.write(';'.join([str(e) for e in l]) + '\n')
    
    	idRow += 1