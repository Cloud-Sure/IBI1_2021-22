n=1 #Set an initial value
while ((n**2+n+2)/2)<999: #Set a loop, but not the number here
    if ((n**2+n+2)/2)<64:
        print('Cut'+str(n)+'straight lines, we well get'+str((n**2+n+2)/2)+'pieces of pizza. but we steel need more!' )
        n+=1
    else:
        print('Cut'+str(n)+'straight lines, we well get'+str((n**2+n+2)/2)+'pieces of pizza. it is enough for us!' )
        break #Terminate the loop here
