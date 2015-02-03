## Script for mothur users

This script takes the output from mothur's bin.seqs command and turns it into something similar to the output from Qiime's pick_otus.py command, which can then be used with the MED-Paper-Figure-6 scripts

The bin.seqs command in mothur should be used as follows:
bin.seqs(list=YOURFILE.list, fasta=YOUFILE.fasta, label=0.03)  
output: YOURFILE.0.03.fasta

This script can then be used as follows:  
python mothurToQiime.py YOURFILE.0.03.fasta

The output (OTUseqID.txt) can then be used as QIIME_OTUs_FILE_PATH in 00_gen_otu_dict.py
