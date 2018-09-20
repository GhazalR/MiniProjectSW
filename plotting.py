import time
import random
import matplotlib.pyplot as plt, mpld3

"""
time=[1,2,3,4,5]
value = [60, 65,62,60,67]

"""

#arrays for humidity and temperature for the three homes
humiditylist = [0,0,0]
templist = [60,61,65]

class house:
    owner = ""
    ID = ""
    temp = 0
    hum = 0
    temp_hist = []
    hum_hist = []

"""
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
"""

counter = 0
counter2 = 0
time_temp = [1,2,3]
time_hum = [7,8,9]
#makes sure only incrementing one of the three temperatures

for x in range(0,len(templist)):
    if templist[counter] <=75:
        templist[counter] +=1
    else:
        templist[counter] -=1
    if counter <=1:
        counter +=1
    else:
        counter = 0

for x in range(0,len(humiditylist)):
    humiditylist[counter2] = random.randint(30,90)
    counter2 += 1

"""
print(templist)
print(humiditylist)
"""
plt.figure(1)

plt.subplot(211)
plt.title('Temperature vs Time (in F)')
plt.plot(time_temp,templist)

plt.subplot(212)
plt.title('Humidity vs Time (%)')
plt.plot(time_hum,humiditylist)

plt.subplots_adjust(left=.125, right = .9,  bottom=.05, top=.9, wspace=.2, hspace=.2)

mpld3.show()

