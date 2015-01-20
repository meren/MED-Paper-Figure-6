import os
import sys
import Oligotyping.lib.fastalib as u
import cPickle

read_id_to_node = {}
node_to_read_ids = {}

# This is a bit tricky. There are two files you need to replace in this Python
# script. The first one is right down below, 'NODE_IDS_OF_INTEREST'. This file
# lists all the node IDs you are interested in visualizing. For instance top
# 100 most abundant nodes. To keep the visualization simpler and
# comprehensible. It is pretty straightforward, and here is an example to show
# how it looks:
#
#000005591
#000004955
#000003105
#000005530
#000003465
#000003684
#000005301
#000001012

nodes = [x.strip() for x in open(NODE_IDS_OF_INTEREST).readlines()]

for node in nodes:
    print node

    # So this is the other thing that needs to be replaced. You must replace
    # the word 'PATH_TO_MED_ANALYSIS_RESULTS' with the MED analysis
    # output path --the path in which you see all the output files like
    # MATRIX-COUNT.txt or directories like HTML-OUTPUT..
    fasta = u.SequenceSource(os.path.join(PATH_TO_MED_ANALYSIS_RESULTS, 'NODES/%s.fa' % node))

    node_to_read_ids[node] = []

    while fasta.next():
        read_id = fasta.id.split('|')[0]

        node_to_read_ids[node].append(read_id)
        read_id_to_node[read_id] = node

    fasta.close()

cPickle.dump(read_id_to_node, open('read_id_to_node.cPickle', 'w'))
cPickle.dump(node_to_read_ids, open('node_to_read_ids.cPickle', 'w'))
