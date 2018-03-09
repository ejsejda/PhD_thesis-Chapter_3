####        REMOVING SEQUENCES REDUNDANCY          #####
###    This code was used in chapter 3 for removing  ### 
###    PHI-base version 3.2 redundant sequences      ###
########################################################
import sys   
#class declaration with both attributes we need   
class Fasta:   
    def __init__(self, name, sequence):   
        #this will store the sequence name   
        self.name = name   
        #this  will store the sequence itself   
        self.sequence = sequence   
  
#this function will receive the list with the file   
#contents, create instances of the Fasta class as   
#it scans the list, putting the sequence name on the   
#first attribute and the sequence itself on the second   
#attribute   
def read_fasta(file):   
    #we declare an empty list that will store all   
    #Fasta class instances generated   
    items = []   
    index = 0  
    for line in file:   
    #we check to see if the line starts with a > sign   
        if line.startswith(">"):   
           #if so and our counter is large than 1   
           #we add the created class instance to our list   
           #a counter larger than 1 means we are reading   
           #from sequences 2 and above   
           if index >= 1:   
               items.append(aninstance)   
           index+=1  
           #we add the line contents to a string   
           name = line[:-1]
           #name = name.split("|")   
           #and initialize the string to store the sequence   
           seq = ''  
           #this creates a class instance and we add the attributes   
           #which are the strings name and seq   
           aninstance = Fasta(name, seq)   
        else:   
           #the line does not start with > so it has to be   
           #a sequence line, so we increment the string and   
           #add it to the created instance   
            seq += line[:-1]   
            aninstance = Fasta(name, seq)   
  
    #the loop before reads everything but the penultimate   
    #sequence is added at the end, so we need to add it   
    #after the loop ends   
    items.append(aninstance)   
    #a list with all read sequences is returned   
    return items   
  
def removeBlank(name):
    
    print "Removing blanks"
    
    fileName =("/home/janowska/Projects/PHI-base/%s" %(name))
    fastafile = open(fileName).readlines()
    mysequences = read_fasta(fastafile)  

    blankName=("/home/janowska/Projects/PHI-base/noBlank_%s" %(name))
    
    nonBlankFastaFile = open(blankName, "w")

    for i in mysequences:
        nonBlankFastaFile.write(i.name.replace(' ','_') + '\n')  
        nonBlankFastaFile.write(i.sequence + '\n')


    nonBlankFastaFile.close()
    
def nonRedFastaSeq(name):
    print "Removing redundant sequences"
    
    fileName =("/home/janowska/Projects/PHI-base/%s" %(name))
    fastafile = open(fileName).readlines()
    mysequences = read_fasta(fastafile)  
    
    nonRedundantName=("/home/janowska/Projects/PHI-base/nonRed_%s" %(name))
    nonRedFastaFile=open(nonRedundantName, "w")
    s = set()
    print "Original file has %d sequences" % len(mysequences) 
    index =1
    for i in mysequences:
        #if third element of the name doesn't exist
        if (i.name.split("|")[2]) not in s:
            #Non_RedFastaFile.write(str(index))
            nonRedFastaFile.write(i.name + '\n')  
            nonRedFastaFile.write(i.sequence + '\n')
            #add it
            s.add(i.name.split("|")[2])
            index+=1
    print "Non redundant file has %d sequences" % index         
    nonRedFastaFile.close()
##############   MAIN PROGRAM  ###################################
name = "phi_base_3_2_protein.fas"
removeBlank(name)
nonRedFastaSeq(name)  


   