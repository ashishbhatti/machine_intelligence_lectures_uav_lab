import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendancerealtime-271223-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "1":
        {
            "name": "Ashish",
            "major": "Aerospace Engineering",
            "starting_year": 2016,
            "total_attendance": 6,
            "standing": "G",
            "year": 6,
            "last_attendance_time": "2023-12-26 00:54:34"
        },
    "2":
        {
            "name": "Bill Gates",
            "major": "Computer Science",
            "starting_year": 1973,
            "total_attendance": 6,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-26 00:54:34"
        },
    "3":
        {
            "name": "Elon Musk",
            "major": "Economics",
            "starting_year": 1992,
            "total_attendance": 6,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2022-12-26 00:54:34"
        },
    "4":
        {
            "name": "Emma Stone",
            "major": "None",
            "starting_year": 2002,
            "total_attendance": 6,
            "standing": "B",
            "year": 1,
            "last_attendance_time": "2022-12-26 00:54:34"
        },
    "5":
        {
            "name": "Jeff Bezos",
            "major": "Computer Science",
            "starting_year": 1982,
            "total_attendance": 6,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-26 00:54:34"
        },
}

for key, value in data.items():
    ref.child(key).set(value)
