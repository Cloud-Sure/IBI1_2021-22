import re #import re function
origin_file = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r') #open file as a reading one

file_name = input('please write a filename as the new fasta file to be written to:')
output_file = open(file_name, 'w')

nwedir = {}

for line in origin_file:
    line = line.rstrip()  #copy the string in file and store it
    if line.startswith('>'):
        gene = re.search(r'gene:(.+?\s)', line)
        gene_seq = '\n' + '>' + gene.group(1)
        nwedir[gene_seq] = " "  #if the line is gene name, it will become white space
    else:
        nwedir[gene_seq] = nwedir[gene_seq] + line #if the line is gene sequence, it will be put into the dirtionary
for i in nwedir.keys():
    if re.search('GAATTC',nwedir[i]):
        target_DNA = re.findall('GAATTC', nwedir[i])
        fragment = str(len(nwedir[i]) + 1)  #caculate the fragments of selected DNA after being cut
        DNA_and_fragment = i + " " + fragment
        DNA_and_number = DNA_and_fragment.strip()
        output_file.write(DNA_and_number + nwedir[i] + '\n')