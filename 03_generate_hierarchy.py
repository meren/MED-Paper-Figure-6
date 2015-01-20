import cPickle

node_to_read_ids   = cPickle.load(open('node_to_read_ids.cPickle'))
otu_id_to_read_ids = cPickle.load(open('otu_id_to_read_ids.cPickle'))
read_id_to_node    = cPickle.load(open('read_id_to_node.cPickle'))
read_id_to_otu_id  = cPickle.load(open('read_id_to_otu_id.cPickle'))
read_id_to_taxa    = cPickle.load(open('read_id_to_taxa.cPickle'))
taxa_to_read_ids   = cPickle.load(open('taxa_to_read_ids.cPickle'))

nodes = [x.strip() for x in open('02_MED_nodes_by_freq.txt').readlines()]

relations = {}

for node in nodes:
    print node
    for read_id in node_to_read_ids[node]:
        relation = '%s,%s,%s' % (read_id_to_taxa[read_id], read_id_to_otu_id[read_id], node)
        if relations.has_key(relation):
            relations[relation] += 1
        else:
            relations[relation] = 1

cPickle.dump(relations, open('relations.cPickle', 'w'))
