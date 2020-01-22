from firebase_admin import db
from requests import get

json_url = 'https://storage.googleapis.com/ds_data_import/chicago_bulls_1995_1996.json'
chicago_bulls_dict = get(json_url).json()
root = db.reference()
root.child('chicago_bulls').push(chicago_bulls_dict)