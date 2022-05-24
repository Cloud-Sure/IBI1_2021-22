import re
seq = 'ATGCAATCGACTACGATCAATCGAGGGCC'
x = re.findall('GAATTC',seq)
print("The number of the fragment is "+str(len(x)+1))