import random

#arrays for humidity and temperature for the three homes
humiditylist = [0,0,0]
templist = [60,60,60]

#if temp is below 60, go up to 75
#if temp is above 75, scale down to 60
counter = 0

#makes sure only incrementing one of the three temperatures

for x in range(0,9):
    print(counter)
    if templist[counter] <=75:
        templist[counter] +=1
    else:
        templist[counter] -=1
    if counter <=1:
        counter +=1
    else:
        counter = 0

print(templist)

#this is 