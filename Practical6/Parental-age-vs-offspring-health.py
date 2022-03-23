import matplotlib.pyplot as plt
import numpy as np

paternal_age=[30,35,40,45,50,55,60,65,70,75]
chd=[1.03,1.07,1.11,1.17,1.23,1.32,1.42,1.55,1.72,1.94]

x = np.array([paternal_age])
y = np.array([chd])

plt.title("the relative risk for congenital heart disease") # set title
plt.xlabel('paternal_age') # set  x axis name
plt.ylabel('chd') # set  y axis name
plt.scatter(x, y)
print([paternal_age])
print([chd])

plt.show()

d1= dict(zip(paternal_age,chd)) #Merge two lists into one dictionary

print('Please enter the given pateral age')
x=int(input()) #Enter the given pateral age

d1[x] 
