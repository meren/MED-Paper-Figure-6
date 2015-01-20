import cPickle

read_id_to_taxa = {}
taxa_to_read_ids = {}

# you need to replace READ_ID_TO_TAXON_FILE_PATH in the following line with a TAB-delimited text file that shows
# the taxon assignment for each read id in the FASTA file. 
#
# here is a couple of lines to clarify how this file should look like:
#
#147406386-PT_GFKBOSR02G7LTI Bacteria;Actinobacteria;Actinobacteria;Coriobacteriales;Coriobacteriaceae;Atopobium
#147406386-PT_GFKBOSR02G8Z5J Bacteria;Actinobacteria;Actinobacteria;Actinomycetales;Actinomycetaceae;Actinomyces
#147406386-PT_GFKBOSR02G9WX7 Bacteria;Actinobacteria;Actinobacteria;Actinomycetales;Actinomycetaceae;Actinomyces
#147406386-PT_GFKBOSR02GAGW4 Bacteria;Actinobacteria;Actinobacteria;Actinomycetales;Micrococcaceae;Rothia
#147406386-PT_GFKBOSR02GBOY1 Bacteria;Actinobacteria;Actinobacteria;Actinomycetales;Micrococcaceae;Rothia
#147406386-PT_GFKBOSR02GEMTS Bacteria;Actinobacteria;Actinobacteria;Coriobacteriales;Coriobacteriaceae;Atopobium
#147406386-PT_GFKBOSR02GFZBS Bacteria;Actinobacteria;Actinobacteria;Actinomycetales;Actinomycetaceae;Actinomyces
#

for read_id, taxon in [l.strip().split('\t') for l in open(READ_ID_TO_TAXON_FILE_PATH).readlines()]:
    if taxa_to_read_ids.has_key(taxon):
        taxa_to_read_ids[taxon].append(read_id)
    else:
        taxa_to_read_ids[taxon] = [read_id]

    read_id_to_taxa[read_id] = taxon


cPickle.dump(read_id_to_taxa, open('read_id_to_taxa.cPickle', 'w'))
cPickle.dump(taxa_to_read_ids, open('taxa_to_read_ids.cPickle', 'w'))
