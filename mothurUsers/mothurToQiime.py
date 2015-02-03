import sys

# script to take the output from mothur's bin.seqs command and turn it into the output from Qiime's pick_otus.py command
# this output can then be used with the MED-Paper-Figure-6 scripts

# the bin.seqs command in mothur should be used as follows:
# bin.seqs(list=YOURFILE.list, fasta=YOUFILE.fasta, label=0.03)
# output: YOURFILE.0.03.fasta

# this script can then be used as follows:
# python mothurToQiime.py YOURFILE.0.03.fasta
# the output (OTUseqID.txt) can then be used as QIIME_OTUs_FILE_PATH in 00_gen_otu_dict.py


binSeqs_handle = sys.argv[1]
output_handle = open("OTUseqID.txt", "w")

seqDict = {}
seqCount = 0
otuCount = 0

with open(binSeqs_handle) as f:
	for line in f:
		if line.startswith('>'):
			seqCount += 1
			line = line.strip()
			cols = line.split()
			seqID = cols[0].lstrip('>')
			otuNum = cols[1]
			if otuNum not in seqDict:
				otuCount += 1
				seqDict[otuNum] = [seqID]
			else:
				seqDict[otuNum].append(seqID)

print "you have %d sequences and %d OTUs" % (seqCount, otuCount)

for j in seqDict:
	output_handle.write(j + '\t' + '\t'.join(seqDict[j]) + '\n')










