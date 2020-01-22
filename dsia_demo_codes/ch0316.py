import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate('PATHTOYOURSERVICEACCOUNT') # 替換成自己的 Service Account 本機位址
firebase_admin.initialize_app(cred, {
    'databaseURL' : 'YOURDATABASEURL' # 替換成自己的 Firebase 網址
})