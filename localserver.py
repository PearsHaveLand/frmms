from flask import Flask, request, render_template
import pyrebase
app = Flask(__name__)

import pyrebase

config = {
  "apiKey": "AIzaSyAJa-17y_cqUGGq3bvYjCM2PLDwxI2a_i4",
  "authDomain": "cmsc447-af201.firebaseapp.com",
  "databaseURL": "https://cmsc447-af201.firebaseio.com/", #check                
  "storageBucket": "cmsc447-af201.appspot.com",
  "serviceAccount": "cmsc447-af201-22ab2aceacc0.json"
}

firebase = pyrebase.initialize_app(config)

try:
    print(firebase.auth().sign_in_with_email_and_password("A","B"))
except:
    print("a")
#print(



@app.route('/')
def my_form():
    print("A")
    return render_template('mockupSign-In.html')

@app.route('/', methods=['POST'])
def my_form_post():
    print("test")
    read = request.form

    print(len(read))
    print((read))
    
    #signing in
    print("pre")
    print(len(read))
    if len(read) == 2:
        print("A")
        username = read['username']
        password = read['password']
        auth = firebase.auth()
        login = "successful login"
        user = None
        try:

            user=auth.sign_in_with_email_and_password(username, password)
        except:
            login = "you suck and i hate you"
        db = firebase.database()
        return render_template('mockupSign-In.html', value=login)
    #new account
    if (len(read) == 4):
        username = read['username']
        passwordd = read['password']
        phoneNum = read['phoneNum']
        id = read['id']
        return render_template('mockupSign-In.html', value="success")
#    return processed_text
if __name__ == '__main__':
    app.run(use_reloader=True, debug=True)

 
