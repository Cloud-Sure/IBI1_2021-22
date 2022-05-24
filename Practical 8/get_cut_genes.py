import re

file=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
gene=file.read()

genelist=re.compile(r'gene:(\S+).*?](.*?)>',re.S)

g=genelist.findall(gene)
new_file=open('cut_genes.fa','w')

for i in range(len(g)):
    new=re.sub(r'\n','',g[i][1])
    
    if "GAATTC" in new:
        new_file.write(">"+g[i][0]+"\n"+str(len(new))+"\n"+new+"\n")