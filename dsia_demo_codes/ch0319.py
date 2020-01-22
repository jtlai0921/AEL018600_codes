from firebase_admin import db

ref = db.reference('chicago_bulls')
chicago_bulls = ref.get()
chicago_bulls