import os
import json
import datetime

from flask import Flask, url_for, redirect, \
    render_template, session, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_required, login_user, \
    logout_user, current_user, UserMixin
from requests_oauthlib import OAuth2Session
from requests.exceptions import HTTPError

from flask import Flask, request
import time
import random
import matplotlib.pyplot as plt, mpld3


basedir = os.path.abspath(os.path.dirname(__file__))

"""App Configuration"""


class Auth:
    """Google Project Credentials"""
    CLIENT_ID = ('906365501211-855a4sktfe0isgs5on4t6ep46n5b2bu1.apps.googleusercontent.com'
)
    CLIENT_SECRET = 'Jon-v9rPIaswzXrU096umuCQy'
    REDIRECT_URI = 'http://localhost:5000/gCallback'
    AUTH_URI = 'https://accounts.google.com/o/oauth2/auth'
    TOKEN_URI = 'https://accounts.google.com/o/oauth2/token'
    USER_INFO = 'https://www.googleapis.com/userinfo/v2/me'
    SCOPE = ['profile', 'email']


class Config:
    """Base config"""
    APP_NAME = "Test Google Login"
    SECRET_KEY = os.environ.get("SECRET_KEY") or "somethingsecret"


class DevConfig(Config):
    """Dev config"""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, "test.db")


class ProdConfig(Config):
    """Production config"""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, "prod.db")


config = {
    "dev": DevConfig,
    "prod": ProdConfig,
    "default": DevConfig
}

"""APP creation and configuration"""
app = Flask(__name__)
app.config.from_object(config['dev'])
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.session_protection = "strong"

""" DB Models """


class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=True)
    avatar = db.Column(db.String(200))
    tokens = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow())


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
""" OAuth Session creation """


def get_google_auth(state=None, token=None):
    if token:
        return OAuth2Session(Auth.CLIENT_ID, token=token)
    if state:
        return OAuth2Session(
            Auth.CLIENT_ID,
            state=state,
            redirect_uri=Auth.REDIRECT_URI)
    oauth = OAuth2Session(
        Auth.CLIENT_ID,
        redirect_uri=Auth.REDIRECT_URI,
        scope=Auth.SCOPE)
    return oauth


@app.route('/')
@login_required
def plotting():
    return render_template('plotting.html')


@app.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    google = get_google_auth()
    auth_url, state = google.authorization_url(
        Auth.AUTH_URI, access_type='offline')
    session['oauth_state'] = state
    return render_template('login.html', auth_url=auth_url)


@app.route('/gCallback')
def callback():
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

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
