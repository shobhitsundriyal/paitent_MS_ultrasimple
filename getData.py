import firebase_admin
import google.cloud
from firebase_admin import credentials, firestore
from pid_generate import get_new_pid
from pid_generate import increment_counter

#cred = credentials.Certificate("./ServiceAccountKey.json")
#app = firebase_admin.initialize_app(cred)

#store = firestore.client()

#l1_coll = 'Patients'
#l1_doc = store.collection(l1_coll)

def treating_existing_patient(pid, store):
    basic_data_doc = store.collection('Patients')
    print(basic_data_doc)
    basic_data = basic_data_doc.document(pid)
    print(basic_data)
    details = basic_data.get().to_dict()
    print(details)
    print('----------')
    dia_hist = basic_data.collection('Diagonosis').stream()
    return details, dia_hist