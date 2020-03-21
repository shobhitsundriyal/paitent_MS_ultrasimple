from firebase import firebase


config = {
    'apiKey': "AIzaSyBAziGjDRUBGJa9CB_R4iVo1_A9_EjHntU",
    'authDomain': "tatkaal-e8a1b.firebaseapp.com",
    'databaseURL': "https://tatkaal-e8a1b.firebaseio.com",
    'projectId': "tatkaal-e8a1b",
    'storageBucket': "tatkaal-e8a1b.appspot.com",
    'messagingSenderId': "967129453853",
    'appId': "1:967129453853:web:a2cb80b3d67dda25963df4",
    'measurementId': "G-9FRVLGJKQG"
  }

firebase = firebase.FirebaseApplication('https://your_storage.firebaseio.com', None)
result = firebase.get('/users', None)
print (result)

