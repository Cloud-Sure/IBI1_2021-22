import re
def mRNA_protein(RNA_string):
    '''将mRNA翻译成蛋白质'''
    start_code = 'AUG'
    end_code = ['UAA', 'UAG', 'UGA']
    protein_table = {'UUU': 'F', 'CUU': 'L', 'AUU': 'I', 'GUU': 'V', \
                     'UUC': 'F', 'CUC': 'L', 'AUC': 'I', 'GUC': 'V', \
                     'UUA': 'L', 'CUA': 'L', 'AUA': 'I', 'GUA': 'V', \
                     'UUG': 'L', 'CUG': 'L', 'AUG': 'M', 'GUG': 'V', \
                     'UCU': 'S', 'CCU': 'P', 'ACU': 'T', 'GCU': 'A', \
                     'UCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A', \
                     'UCA': 'S', 'CCA': 'P', 'ACA': 'T', 'GCA': 'A', \
                     'UCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A', \
                     'UAU': 'Y', 'CAU': 'H', 'AAU': 'N', 'GAU': 'D', \
                     'UAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D', \
                     'UAA': 'Stop', 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E', \
                     'UAG': 'Stop', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E', \
                     'UGU': 'C', 'CGU': 'R', 'AGU': 'S', 'GGU': 'G', \
                     'UGC': 'C', 'CGC': 'R', 'AGC': 'S', 'GGC': 'G', \
                     'UGA': 'Stop', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G', \
                     'UGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G'
                     }
    #找到起始密码子的位置
    start_sit = re.search(start_code, RNA_string)
    protein = ''
    #按阅读框匹配蛋白质
    for sit in range(start_sit.end(), len(RNA_string), 3):
        protein = protein + protein_table[RNA_string[sit:sit+3]]
    print (protein)
 
if __name__ == '__main__':
    RNA_string = open('E:\\bioinfo\data\\rosalind_prot\\rosalind_prot.txt', 'r').read().strip()
    mRNA_protein(RNA_string)