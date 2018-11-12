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

#try:
#    print(firebase.auth().sign_in_with_email_and_password("A","B"))
#except:
#    print("a")
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
    print(read)
    auth = firebase.auth()
    if read['TYPE'] == 'CNEO':
        print("A")
    elif read['TYPE'] == 'SIEU':
        print("A")
        username = read['email']
        password = read['password']
        print("B")
        login = "successful login"
        user = None
        try:
            user=auth.sign_in_with_email_and_password(username, password)
        except:
            login = "login failed"
        db = firebase.database()
        return render_template('operationsDashboard.html', value=login)
    #new account
    elif read['TYPE'] == 'CU':
        print(read)
        username = read['email']
        password = read['password']
        phoneNum = read['phoneNum']
        id = read['id']
        department = read['department']
        try:
            auth.create_user_with_email_and_password(username, password)
            user = auth.sign_in_with_email_and_password(username, password)
            db = firebase.database()
            db.child("users").push({"email":username, "password":password, "phonenumber":phoneNum, "id":id, "department":department}, user['idToken'])
        except:
            
            return render_template('mockupSign-In.html', value="failed account creation")
        return render_template('mockupSign-In.html', value="success")
#    return processed_text
if __name__ == '__main__':
    app.run(use_reloader=True, debug=True)
