from flask import Flask, request
import time
import random
import matplotlib.pyplot as plt, mpld3
from matplotlib.font_manager import FontProperties


app = Flask(__name__)

@app.route('/')
def main():
    return """<html>
                   <head>
                   <style>
                   body {
                       background-color: #80acf2;
                   }
                   </style>
                      <script type="text/javascript" src="http://code.jquery.com/jquery-1.11.1.min.js"></script>
                      <script>
                           $(document).ready(function(){

                                $('#btnSend').click(function(){

                                    $.ajax({
                                      type: 'POST',
                                      url: '/process',
                                      success: function(data){
                                        alert(data);
                                      }
                                    });
                                });
                                $('#btnSend2').click(function(){

                                    $.ajax({
                                      type: 'POST2',
                                      url: '/process',
                                      success: function(data){
                                        alert(data);
                                      }
                                    });
                                });
                           });
                      </script>
                   </head>
                   <body>
                    <h1 style="text-align:center;"> Welcome to Home Sensor Homepage</h1> 
                    <h3 style="text-align:center;"> By Biagio DeSimone & Ghazal Randhawa </h3> 
                    <div style="text-align:center;">
                        <input type="button" id="btnSend" value="Show Temperature and Humidity Graphs">
                        <input type="button" id="btnSend2" value="Add Additional Temperature And Humidity Sensor">    
                    </div>                
                    </body>
                   </html>"""
#added comment 

@app.route('/process', methods=['POST','POST2'])
def view_do_something():

    if request.method == 'POST':
        #your database process here
        humiditylist = [0,0,0,0,0,0,0]
        templist = [60,61,65,64,63,63,62]
        counter = 0
        counter2 = 0
        time_temp = [1,2,3,4,5,6,7]
        time_hum = [1,2,3,4,5,6,7]
        #makes sure only incrementing one of the three temperatures

        for y in range(0,len(templist)):
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


        plt.figure(1)
        plt.subplot(211)
        plt.title('Temperature vs Time Sensor 1')
        plt.subplot(211).set_ylabel('Temperature (F)')
        #plt.suptitle('Living Room Sensors', fontsize = 16)
        plt.plot(time_temp,templist)

        plt.subplot(212)
        plt.title('Humidity % vs Time Sensor 1')
        plt.subplot(212).set_ylabel('Humidity (%)')
        plt.plot(time_hum,humiditylist)

        plt.subplots_adjust(left=.125, right = .9,  bottom=.05, top=.9, wspace=.2, hspace=.2)

        mpld3.show()
        return "OK"
    if request.method == 'POST2': 
        #your database process here
        humiditylist = [0,0,0,0,0,0,0]
        templist = [60,61,65,64,63,63,62]
        counter = 0
        counter2 = 0
        time_temp = [1,2,3,4,5,6,7]
        time_hum = [1,2,3,4,5,6,7]
        #makes sure only incrementing one of the three temperatures

        for y in range(0,len(templist)):
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


        plt.figure(2)
        plt.subplot(221)
        plt.title('Temperature vs Time Sensor 2')
        plt.subplot(221).set_ylabel('Temperature (F)')
        #plt.suptitle('Living Room Sensors', fontsize = 16)
        plt.plot(time_temp,templist)

        plt.subplot(222)
        plt.title('Humidity % vs Time Sensor 2')
        plt.subplot(222).set_ylabel('Humidity (%)')
        plt.plot(time_hum,humiditylist)

        plt.subplots_adjust(left=.125, right = .9,  bottom=.05, top=.9, wspace=.2, hspace=.2)

        mpld3.show()
        return "OK"
    else:
        return "Error"

if __name__ == '__main__':
    app.run()