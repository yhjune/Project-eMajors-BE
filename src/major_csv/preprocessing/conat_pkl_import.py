import pickle
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from pathlib import Path
import os

def result_course_doc(dataframe):
    for row in df.itertuples():
        course_id, department_id = row.course_id, row.department
        course_name, classification, credit,academic_year,area,semester,note = row.course_name, row.classification, row.credit, row.academic_year,row.area,row.semester,row.note
        course_name_eng, intro_kr, intro_eng = row.course_name_eng, row.intro_kr, row.intro_eng
        course = {
            "_id":{
                "course_id" : course_id,
                "department_id" : department_id
            },
            "course_name" : course_name,
            "classification":classification,
            "credit":credit,
            "academic_year": academic_year,
            "area":area,
            "semester":semester,
            "note":note,
            "intro":{
                "intro_kr": intro_kr,
                "intro_eng": intro_eng ,
                "course_name_eng" : course_name_eng
            }
        }
        course_collection.insert_one(course)


with open(file="result.pickle",mode='rb') as data:
    df = pickle.load(data)

print("result succesfully load")

load_dotenv()
# Replace the placeholder with your Atlas connection string
uri = os.getenv("DB_URI")

# Set the Stable API version when creating a new client
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# DB connections setting
db = client['erode']
course_collection = db['course_v2']
print("...Inserting course intro documnets into MongoDB...")
result_course_doc(df)
print("ok")