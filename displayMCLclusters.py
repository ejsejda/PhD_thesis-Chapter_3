#######################################################################################
###  This script was used to produce picture of MCL clusters or single MCL cluster  ###
###  It uses output files created with python scripts:                              ###
###                                     gettingHostTaxa_fromPHIbase_4.0.py          ###
###                                     analysisOfPHIbase_v4.0.py                   ###
#######################################################################################

from numpy import *
from numpy.lib.io import loadtxt
import networkx as nx
import matplotlib.pyplot as plt

projectDir1="/home/ela/Project/PHI-base4.0-analysis/output"
def getColorandSize(nodes, d, s):
	colorList=list()
    	sizeList=list()
     	for n in nodes:
			if 'Plant Pathogen' in d[n] and 'Animal Pathogen' in d[n]:
            	c='y'
			elif 'Plant Pathogen' in d[n] and 'Other Pathogen' in d[n]:
				c = 'r'
			elif 'Animal Pathogen' in d[n] and  'Other Pathogen' in d[n]:
				c = 'b'
        	elif 'Plant Pathogen' in d[n]:
            	c='g'
        	elif 'Animal Pathogen' in d[n]:
            	c='c'     
        	elif 'lethal' in d[n]:
            		c='w'
        	elif 'chem target' in d[n]:
            		c='orange'   
        	elif 'Other Pathogen' in d[n]:
            		c='m'
        	colorList.append(c)
             
        	if s.has_key(n):
            		sizeList.append(int(s[n]))
        	else:
            		sizeList.append(0)   
    	return colorList, sizeList
	
fileName1="MCL_1.6_OutputModified.txt" % (projectDir1) #output file from MCL clustering
fileName2="phiBase_version4.0_content.txt" % (projectDir1)#file created with script: gettingHostTaxa_fromPHIbase_4.0.py
fileName3="pathClassOnGeneId_PHIid_phiBase_4.0.csv.csv" % (projectDir1) #file created with script: analysisOfPHIbase_v4.0.py
#Read the cluster information into an array
data1=loadtxt(fileName1, dtype='S')
data2=loadtxt(fileName2, dtype='S', delimiter=';')
#d=dict([(e.split(';')[0], e.split(';')[7]) for e in data2])
d=dict()
for e in data2:
    k='PHI:'+e[0]
    v=e[7]
    d.setdefault(k, set()).add(v)
data3=loadtxt(fileName3, dtype='S', delimiter=';')
s=dict([('PHI:'+e[0], e[1]) for e in data3])
#Create an empty dictionary
cluster=dict()
phi=dict()
G=nx.Graph()
#For each element of the array, that is for each line of the file
for row in data1: 
    #Get the cluster Id
    idCluster=int(row[0])-1
    #Get the information
    info1=row[1].split('|')[0] 
    if not cluster.has_key(idCluster):
        cluster[idCluster]=list()   
    cluster[idCluster].append(info1)

for idCluster in arange(len(cluster)):
	for g1 in cluster[idCluster]:
		for g2 in cluster[idCluster]:
			if g1 != g2:
				G.add_edge(g1,g2)
   
colorList, sizeList = getColorandSize(G.nodes(), d, s)

plt.figure(1,figsize=(12,12))
# layout graphs with positions using graphviz neato
pos=nx.graphviz_layout(G,prog="neato")
C=nx.connected_component_subgraphs(G) # for displaying all clusters without nodes label
#Use below for displaying single cluster with nodes labeled, where C[0]-1st largest cluster, C[1]- second largest cluster and so on
#nx.draw(C[0], with_labels=True, node_size=array(sizeList)*1800, node_color=colorList, alpha=1.0)
nx.draw(G, pos,with_labels=False, node_size=array(sizeList)*50,node_color=colorList, alpha=1.0)
plt.show()

   
 





    
    

    

     
