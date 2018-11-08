from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"



import pyrebase
config = {
  "apiKey": "AIzaSyAJa-17y_cqUGGq3bvYjCM2PLDwxI2a_i4",
  "authDomain": "cmsc447-af201.firebaseapp.com",
  "databaseURL": "https://cmsc447-af201.firebaseio.com/", #check
  "storageBucket": "cmsc447-af201.appspot.com",
  "serviceAccount": "cmsc447-af201-22ab2aceacc0.json"
}
firebase = pyrebase.initialize_app(config)

auth = firebase.auth()
#authenticate a user
user = auth.sign_in_with_email_and_password("jberns1@umbc.edu", "testtest")
#user = auth.sign_in_with_email("jberns1@umbc.edu")
print(user['idToken'])
db = firebase.database()

def addEvent(urgency, location, mission, team, time, status, notes, assigner):
    event = {"urgency":urgency, "location":location, "mission":mission, "team":team, "time":time, "status":status, "notes":notes, "assigner":assigner}
    db.child("event").push(event, user['idToken'])

def addMission(events, status, assigner):
    mission = {"events":events, "status":status, "assigner":assigner}
    db.child("mission").push(mission, user['idToken'])

def initialize(user):
    mission = {"events": "", "status":"Boolean", "assigner":""}
    db.child("mission").push(mission, user['idToken'])

    event = {"urgency": "integer", "location": "", "mission" : "", "team":"", "time":"", "status":"", "notes":"", "assigner":""}
    db.child("event").push(event, user['idToken'])

#archer = {"name": "Sterling Archer", "agency": "Figgis Agency"}
initialize(user)

#db.child("agents").push(archer, user['idToken'])
if __name__ == '__main__':
    app.run()
