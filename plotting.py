import random
import matplotlib.pyplot as plt
#arrays for humidity and temperature for the three homes
humiditylist = [0,0,0]
templist = [60,60,60]

class house:
    owner = ""
    ID = ""
    temp = 0
    hum = 0
    temp_hist = []
    hum_hist = []


Home1 = house()
Home2 = house()
Home3 = house()

Home1.owner = "Biagio"
Home2.owner = "Ghazal"

Home1.temp = random.uniform(50,80)
Home2.temp = random.uniform(50,80)

print(Home1.owner)
print(Home2.owner)
print(Home1.temp)
print(Home2.temp)


#if temp is below 60, go up to 75
#if temp is above 75, scale down to 60
counter = 0

#makes sure only incrementing one of the three temperatures

f""" or x in range(0,9):
    print(counter)
    if templist[counter] <=75:
        templist[counter] +=1
    else:
        templist[counter] -=1
    if counter <=1:
        counter +=1
    else:
        counter = 0
"""
list = [2,3,4,5]
plt.plot(list)
plt.ylabel('temperature')

#used to get graph to show, click enter to get rid of it 
plt.show(block=False)
input('press <ENTER> to continue')
