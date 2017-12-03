'''
Created on 11 May 2010

@author: janowska
'''
############################################################################################################
###   This program uses as input file the file created with "gettingHostTaxa_fromPHIbase_4.0.py", namely  ###
###   input file: "phiBase_version4.0_content.txt". Then, the number of hosts and genes are calculated   ###
###   for particular species belonging to either plant, animal or other pathogens.                       ###
############################################################################################################
from numpy import *
import csv

fh = open("/home/janowska/Projects/PHI-base/phiBase_version4.0_content.txt")
data = fh.read()
fh.close()

rows=[row.split(';') for row in data.split('\n') if not row=='']
 
dK=dict()
dInteractionTaxa=dict()
dInteractionK=dict()
dHostTaxaId=dict()
dPhiGeneId=dict()
for r in rows:
    taxaName=r[2]#pathogen name
    hostKingdom=r[7]
    phiGeneId=r[0]
    hostTaxaId=r[4]#host id
 #assigning pathogen to Kingdom    
    if not dK.has_key(taxaName):
        dK[taxaName]=hostKingdom
  #assigning all interactions per pathogen               
    if not dInteractionTaxa.has_key(taxaName):
        dInteractionTaxa[taxaName]=1   
    else:
        dInteractionTaxa[taxaName] +=1
  #assigning unique numger of host pathogen interact
    if not dHostTaxaId.has_key(taxaName):
        dHostTaxaId[taxaName]=set([hostTaxaId])    
    else:
        dHostTaxaId[taxaName].add(hostTaxaId)
   

    if not dPhiGeneId.has_key(taxaName):
        dPhiGeneId[taxaName]=set([phiGeneId])    
    else:
        dPhiGeneId[taxaName].add(phiGeneId)

    if not dInteractionK.has_key(hostKingdom):
        dInteractionK[hostKingdom]=1
    else:
        dInteractionK[hostKingdom] +=1
    


fh = open("/home/janowska/Projects/PHI-base/PlantPathogenHostgeneNo_phiBase_4.0.csv", "w")
writer=csv.writer(fh, delimiter="\t")
rows=[(i,len(dHostTaxaId[i]), len(dPhiGeneId[i]), dInteractionTaxa[i]) for i in sort(dHostTaxaId.keys()) if dK[i]=='Plant Pathogen']
for r in rows:
    writer.writerow(r)
fh.close()

fh = open("/home/janowska/Projects/PHI-base/AnimalPathogenHostgeneNo_phiBase_4.0.csv", "w")
writer=csv.writer(fh, delimiter="\t")
rows=[(i,len(dHostTaxaId[i]),len(dPhiGeneId[i]), dInteractionTaxa[i]) for i in sort(dHostTaxaId.keys()) if dK[i]=='Animal Pathogen']
for r in rows:
    writer.writerow(r)
fh.close()

fh = open("/home/janowska/Projects/PHI-base/OtherPathogenHostgeneNo_phiBase_4.0.csv", "w")
writer=csv.writer(fh, delimiter="\t")
rows=[(i,len(dHostTaxaId[i]),len(dPhiGeneId[i]), dInteractionTaxa[i]) for i in sort(dHostTaxaId.keys()) if dK[i]=='Other Pathogen']
for r in rows:
    writer.writerow(r)
fh.close()

#In the output file the number of hosts that particular pathogen interacts is calculated per each PHI-base entry.
#The information from this file is used in MCL cluster display (in "displayMCLclusters.py")
fh = open("/home/janowska/Projects/PHI-base/pathClassOnGeneId_PHIid_phiBase_4.0.csv", "w")
writer=csv.writer(fh, delimiter=";")
rows=[(i,len(dHostTaxaId[i])) for i in sort(dHostTaxaId.keys())]
for r in rows:
    writer.writerow(r)
fh.close()


