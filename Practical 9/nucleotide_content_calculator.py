sequence = 'ATCCCgattgcccctaatGGA'.lower()#Converting uppercase to lowercase letters in a string

ratio = {'a':0,'t':0,'c':0,"g":0} #The initial ratio is zero

def calculator(sequence):
    amount = 0
    for i in sequence:
        ratio[i] += 1
        amount += 1
        
    for i in 'atcg':
        ratio[i] /= amount
        
calculator(sequence)
print(ratio)