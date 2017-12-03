########################################################################
###                     blastparse_Evalue.pl                         ###
### This is pearl script used to extract the information from blastp ###
###       on both matched sequences and e-value                      ###
########################################################################
#! /usr/bin/perl
use strict;
use warnings;
use Bio::SearchIO;

my $output = 'D:\Elzbieta\Projects\PHI-base\blastTabEvalue.txt';
unless (open (FILE, "> $output"))
{
print  "Cannot open the file \"blastTab.txt\" to write to !!!\n\n";
}	
my $searchio = new Bio::SearchIO(-format => 'blast',
                                 -file   => $ARGV[0]);
while( my $result = $searchio->next_result ) {
        my $hit_counter = 0;
        while( my $hit = $result->next_hit ) {
                $hit_counter++;
                    while( my $hsp = $hit->next_hsp ) {
                                print FILE
                                $result->query_name."\t",
                                $hit->accession(),"\t",
                                $hit->significance(),"\n";
                               
                }
         }
 }
########################################################################
###                     removeTrembleseq_Evalue.pl                   ###
### This is pearl script used to remove tremble sequences from the   ###
###                  output of blastparse_Evalue.pl                  ###
########################################################################
#!/usr/bin/perl -w
$inputFile = 'D:\Elzbieta\Projects\PHI-base\blastTabEvalue.txt';
unless (open (BLASTFILE, $inputFile))
{
print "Cannot open the file \"blastTabPrecentId.txt\"\n\n";
}
$outputfile = 'D:\Elzbieta\Projects\PHI-base\phiBaseBlastTabEvalue.txt';
unless (open (FILE, ">$outputfile"))
{
print  "Cannot open the file \"phiBaseBlastTabEvalue.txt\" to write to !!!\n\n";
}
@phiBaseBlast = <BLASTFILE>;
foreach $line (@phiBaseBlast)
{
	@fields = split("\t",$line);
	if($fields[1]!~/^tr\S+/)
	{
		print FILE $line;

	}

 }
close (FILE);
close (BLASTFILE);
exit;

