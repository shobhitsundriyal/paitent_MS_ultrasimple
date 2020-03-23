import firebase_admin
import google.cloud
from firebase_admin import credentials, firestore
from pid_generate import get_new_pid
from pid_generate import increment_counter

cred = credentials.Certificate("./ServiceAccountKey.json")
app = firebase_admin.initialize_app(cred)

store = firestore.client()

l1_coll = 'Patients'
l1_doc = store.collection(l1_coll)

