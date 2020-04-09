import firebase_admin
import google.cloud
from firebase_admin import credentials, firestore
from pid_generate import get_new_pid
from pid_generate import increment_counter
from datetime import date

#cred = credentials.Certificate("./ServiceAccountKey.json")
#app = firebase_admin.initialize_app(cred)

#store = firestore.client()

def push_new_patient(req, store):
    '''Recives dict'''
    today = str(date.today())

    #doc_ref = store.collection(u'test')
    #doc_ref.add({u'name': u'test', u'added': u'just now'})

    l1_coll = 'Patients'
    l1_doc = store.collection(l1_coll)

    pid = get_new_pid()
    p_data =  {
        'PID': pid,
        'Name': req['name'],
        'Address': req['address'],
        'Age':  req['age'],
        'Gender': req['gender'],
        }
    #l1_doc.add(p_data)
    l1_doc.document(pid).set(p_data)
    increment_counter(today, pid[-2:])
    diag = req['diagnosis']
    d = []
    d = diag.split('\n')
    p_diagnosis = {
        'Date':today, 
        'Prov_Diagonis':d
        }
    l1_doc.document(pid).collection('Diagonosis').document(today).set(p_diagnosis)
    if req['p_hist']:
        hist = {
            'Date':'Patient History',
            'Prov_Diagonis':req['p_hist'].split('\n')
        }
        l1_doc.document(pid).collection('Diagonosis').document('00Paytent_hist').set(hist)
    return True

