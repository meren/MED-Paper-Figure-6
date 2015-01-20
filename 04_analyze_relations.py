import cPickle
import math

relations = cPickle.load(open('relations.cPickle'))

# NODE_IDS_OF_INTEREST must be replaced with the corresponding file again. 
nodes = [x.strip() for x in open(NODE_IDS_OF_INTEREST).readlines()]

print 'taxa,otu,med,size'
for node in nodes:
    for k in [x for x in relations.keys() if x.endswith(node)]:
        if relations[k] > 1000:
            print '%s,%d' % (k.split(';')[-1], relations[k])
