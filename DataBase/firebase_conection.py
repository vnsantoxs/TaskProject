import pyrebase

firebaseConfig = {
    "apiKey": "AIzaSyCSL2NTfTR5yJdUA3h9huFmR7fxnRkaCyw",
    "authDomain": "task-64194.firebaseapp.com",
    "projectId": "task-64194",
    "storageBucket": "task-64194.appspot.com",
    "messagingSenderId": "582017876374",
    "appId": "1:582017876374:web:78b9c5a3a0274e893c5db7"
}

app = pyrebase.initialize_app(firebaseConfig)
