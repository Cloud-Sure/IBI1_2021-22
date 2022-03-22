marks=[45,36,86,57,53,92,65,45]
sorted(marks) # returns sorted list, does not mutate L
marks = sorted(marks)
marks.sort() 
print (marks)

import matplotlib.pyplot as plt
import pandas as pd
#plt.figure(figsize=(10,10))
plt.title('marks',fontsize=20)
#data = pd.read(marks)
#labels = 'score'
#box_1=data['marks']

plt.boxplot(marks)

plt.show()

a=sum (marks)/len(marks)
print (a)
if a>60: print('The average mark Rob has received is higher than the pass mark')
if a<60: print('The average mark Rob has received is lower than the pass mark')