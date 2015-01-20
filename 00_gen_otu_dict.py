import cPickle

read_id_to_otu_id = {}
otu_id_to_read_ids = {}

# you need to replace QIIME_OTUs_FILE_PATH with the output qiime 1.5 generates when you use pick_otus.py.
# you can generate that file by hand as well. It simply is a TAB-delimited file that describes which read
# IDs appear in which OTUs.
#
# here is the first 5 lines from such file:
#
#
#0	158337416-KG_GEUHUCK01AX9KK	158337416-KG_GEUHUCK01EIKF3
#1	159227541-SUBP_GD7TPFO01CBGCD	159227541-SUBP_GD7TPFO01DOK9U	159571453-PT_GE8UCXQ02FH7PW
#2	159005010-HP_F6AVU3G01CABT8	159005010-HP_F6AVU3G01EM0UC	159005010-HP_F6AVU3G02HGET3	159005010-HP_F6AVU3G02IOW57
#3	160765029-PT_GEUHUCK02G1T3E	158924089-TD_F6J46LU02GST42
#4	158924089-SUPP_F6J46LU02I7HMQ	160582958-SUPP_GEUHMPI02I6Z3R
#
# the first column is the 'otu id', and it is followed by read IDs appear in the FASTA file.
#

for line in open(QIIME_OTUs_FILE_PATH).readlines():
    fields = line.strip().split('\t')
    otu_id = fields[0]
    read_ids = fields[1:]

    otu_id_to_read_ids[otu_id] = read_ids

    for read_id in read_ids:
        read_id_to_otu_id[read_id] = otu_id


cPickle.dump(read_id_to_otu_id, open('read_id_to_otu_id.cPickle', 'w'))
cPickle.dump(otu_id_to_read_ids, open('otu_id_to_read_ids.cPickle', 'w'))
