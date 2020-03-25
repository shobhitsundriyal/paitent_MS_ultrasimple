# pyrebase authentication to add maybe
from flask import Flask, render_template, request, redirect, url_for
import pdb
import time
from pushData import push_new_patient
from pid_generate import get_new_pid
from getData import treating_existing_patient

import firebase_admin
import google.cloud
from firebase_admin import credentials, firestore

cred = credentials.Certificate("./ServiceAccountKey.json")
app = firebase_admin.initialize_app(cred)

store = firestore.client()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method =='POST':
        if request.form['goto'] == 'new':
            return redirect(url_for('new_patient'))
        if request.form['goto'] == 'old':
            #return redirect(url_for('enter_pid'))
            pass
        if request.form['goto'] == 'getPdata':
            return redirect(url_for('enter_pid_show'))
    return render_template('home.html')

@app.route('/wait')
def wait():
    return render_template('data_added.html')

@app.route('/error')
def error():
    return "Some error occured please try again"

@app.route('/new', methods=['GET', 'POST'])
def new_patient():
    p_id = get_new_pid()
    if request.method =='POST':
        print('Form Data')
        print(dict(request.form))
        scode = False
        scode = push_new_patient(dict(request.form), store)
        if scode:
            return redirect(url_for('wait'))
        else:
            return redirect(url_for('error'))
    return render_template('new_patient.html', p_id=p_id)

@app.route('/enter-pidS', methods=['GET', 'POST'])
def enter_pid_show():
    if request.method == 'POST':
        details = treating_existing_patient(request.form['pid'].strip(' '), store)
        print(str(details))
        det = {}
        det['Address'] = details.get('Address')
        det['Age'] = details.get('Age')
        det['Gender'] = details.get('Gender')
        det['Name'] = details.get('Name')
        det['PID'] = details.get('PID')
        return det
    
    return render_template('enter_Pid.html')

if __name__ == "__main__":
    app.run(debug=True)