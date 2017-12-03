############################################################################################
###   Getting host taxa number from PHI-base version 3.2 and using Entrez database       ###
###        assigning either a host taxonomy name using Entrez database                   ###
############################################################################################
#export http_proxy="http://wwwcache.bbsrc.ac.uk:8080"
import psycopg
import sys
from Bio import Entrez
Entrez.email="elzbieta.janowska-sejda@bbsrc.ac.uk"
#Create the connection to PHI-base database
try:
    phiBasedb = psycopg.connect("host = babvs07.rothamsted.bbsrc.ac.uk dbname= phibase user= phirw")
    print "successful connection"
except StandardError, e:
    print "can't connect to the database", e
    sys.exit()   
#Create a cursor
cursor = phiBasedb.cursor()
#Get multiple rows from a table
print "\n\n PHI_baseID, InteractionID, Host_taxID, Pathogen_taxID" 
cursor.execute("SELECT i. phi_base_fk, i. interaction_id, g.phi_base_acc,  g.name, h.tax_id_fk,p. tax_id_fk, s.syst_name FROM on_host AS h, from_pathogen AS p, interaction AS i, gene AS g, species AS s WHERE h. interaction_fk = p.interaction_fk AND i. interaction_id =h. interaction_fk AND p. tax_id_fk = s.ncbi_tax_id AND i.phi_base_fk = g.phi_base_acc")
rows = cursor.fetchall()
fileName=("/home/janowska/Projects/PHI-base/phiBase_version3.2_content.txt")
phiBazedbQuery=open(fileName, "w")
taxaDict=dict()
idRow=0    
for column in rows:
    print "Processing row nb %d" % idRow
    l= list(column)
    taxaId = column[4]
    if taxaDict.has_key(taxaId):
       records = taxaDict[taxaId]
    else:
        handle = Entrez.efetch(db="Taxonomy", id= taxaId, mode="xml")
        records= Entrez.read(handle)
    if ("Metazoa" in records[0]["Lineage"].split("; ")):
        l.append("Animal Pathogen")           
    elif ("Viridiplantae" in records[0]["Lineage"].split("; ")):
        l.append("Plant Pathogen")         
    else:
        l.append("Other Pathogen")
    phiBazedbQuery.write(';'.join([str(e) for e in l]) + '\n')
    idRow += 1       
phiBazedbQuery.close()
cursor.close()
phiBasedb.close()
sys.exit()
############################################################################################
###   Above code partially reused for getting information from PHI-base version 4.0:     ###
###   Getting host taxa information from flat-file downloaded directly from PHI-base     ###
###   and then accessing Entrez database to define a host taxonomy name                  ###      
############################################################################################
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
        
    
 
