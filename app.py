# pyrebase authentication to add maybe
from flask import Flask, render_template, request, redirect, url_for
import pdb
import time
from pushData import push_new_patient
from pid_generate import get_new_pid

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method =='POST':
        if request.form['goto'] == 'new':
            return redirect(url_for('new_patient'))
        if request.form['goto'] == 'old':
            pass
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
        scode = push_new_patient(dict(request.form))
        if scode:
            return redirect(url_for('wait'))
        else:
            return redirect(url_for('error'))
    return render_template('new_patient.html', p_id=p_id)



if __name__ == "__main__":
    app.run(debug=True)