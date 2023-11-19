from dotenv import load_dotenv
import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from pathlib import Path
import csv_func

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
course_collection = db['course']
courseIntro_collection = db['course_intro']

# ci , dm, m file path recusive
print("...Getting file pahts...")
root = input("root : ") # all files must be nested in the root folder
# output_path = root+"/"+input("output folder name: ")+"/" # exported csv files goes here
# os.makedirs(output_path,exist_ok=True)

# Courser_introduction.pdf
ci_course_docs =[]
ci_courseintro_docs = []
print("...Getting course introductions...")
ci_pdf_files = Path(root).rglob('교과목기술_*.pdf')
for idx, path in enumerate(ci_pdf_files):
    path = str(path)
    ci_name = path.split('/')[-1].split('.')[0]
    print(f'now processing : {ci_name}')
    df = csv_func.transform_funcs.course_intro_df(path)
    ci_course_docs +=csv_func.transform_funcs.ci_course_doc(df)
    ci_courseintro_docs += csv_func.transform_funcs.ci_course_intro_doc(df)

# major.pdf
m_course_docs = []
print("Getting majors...")
m_pdf_path = Path(root).rglob('주전공_*.pdf')
for idx, path in enumerate(m_pdf_path):
    path = str(path)
    m_csv_name = path.split('/')[-1].split('.')[0]
    print(f'now processing : {m_csv_name}')
    df_list, df_condi = csv_func.transform_funcs.major_df(path)
    m_course_docs += csv_func.transform_funcs.m_course_doc(df_list)

#double_major.pdf
dm_course_docs = []
print("...Getting double majors...")
dm_pdf_path =  Path(root).rglob('복수전공_*.pdf')
for idx, path in enumerate(dm_pdf_path):
    path = str(path)
    dm_csv_name = path.split('/')[-1].split('.')[0]
    print(f'now processing : {dm_csv_name}')
    df_list, df_condi = csv_func.transform_funcs.double_major_df(path)
    dm_course_docs += csv_func.transform_funcs.dm_course_doc(df_list)

print("...Inserting course documnets into MongoDB...")
for idx, doc in enumerate(ci_course_docs):
    course_id = doc.get("_id").get("course_id")
    department_id = doc.get("_id").get("department_id")
    filter_criteria = { "_id": {"course_id":course_id, "department_id":department_id}}
    matched_doc = course_collection.find(filter_criteria)
    if matched_doc != None:
        update_C = {"$set":doc.get("update")}
        result1 = course_collection.update_one(filter_criteria,update_C,upsert=True)
    else:
        insert_doc = {
            "_id": {
                "course_id":doc.get("_id").get("course_id"),
                "department_id":doc.get("_id").get("department_id")
            },
            "name" :doc.get("update").get("name"),
            "classification": doc.get("update").get("classification"),
            "credit": doc.get("update").get("credit")
        }
        course_collection.insert_one(insert_doc)

for idx, doc in enumerate(m_course_docs):
    course_id = doc.get("_id").get("course_id")
    department_id = doc.get("_id").get("department_id")
    filter_criteria = { "_id": {"course_id":course_id, "department_id":department_id}}
    matched_doc = course_collection.find(filter_criteria)
    if matched_doc != None:
        update_C = {"$set":doc.get("update")}
        result1 = course_collection.update_one(filter_criteria,update_C,upsert=True)
    else:
        insert_doc = {
            "_id": {
                "course_id":doc.get("_id").get("course_id"),
                "department_id":doc.get("_id").get("department_id")
            },
            "name" :doc.get("update").get("name"),
            "classification": doc.get("update").get("classification"),
            "area":doc.get("update").get("area"),
            "semester":doc.get("update").get("semester"),
            "academic_year": doc.get("update").get("academic_year"),
            "credit": doc.get("update").get("credit")
        }
        course_collection.insert_one(insert_doc)

for idx, doc in enumerate(dm_course_docs):
    course_id = doc.get("_id").get("course_id")
    department_id = doc.get("_id").get("department_id")
    filter_criteria = { "_id": {"course_id":course_id, "department_id":department_id}}
    matched_doc = course_collection.find(filter_criteria)
    if matched_doc != None:
        update_C = {"$set":doc.get("update")}
        result1 = course_collection.update_one(filter_criteria,update_C,upsert=True)
    else:
        insert_doc = {
            "_id": {
                "course_id":doc.get("_id").get("course_id"),
                "department_id":doc.get("_id").get("department_id")
            },
            "name" :doc.get("update").get("name"),
            "classification": doc.get("update").get("classification"),
            "area":doc.get("update").get("area"),
            "semester":doc.get("update").get("semester"),
            "academic_year": doc.get("update").get("academic_year"),
            "credit": doc.get("update").get("credit")
        }
        course_collection.insert_one(insert_doc)

print("...Inserting course intro documnets into MongoDB...")
for idx, doc in enumerate(ci_courseintro_docs):
    course_id = doc.get("_id").get("course_id")
    filter_criteria = { "_id":{"course_id" : course_id}}
    mathched_doc = courseIntro_collection.find(filter_criteria)
    if matched_doc != None:
        update_CI = {"$set":doc.get("update")}
        result2 = courseIntro_collection.update_one(filter_criteria, update_CI, upsert=True)
    else:
        insert_doc={
                "_id":{
                "course_id" : course_id,
                "department_id" : department_id
            },
            "course_name" : doc.get("update").get("course_name"),
            "intro_kr": doc.get("update").get("intro_kr") ,
            "intro_eng": doc.get("update").get("intro_eng") ,
            "course_name_eng" : doc.get("update").get("course_name_eng")
        }
        courseIntro_collection.insert_one(insert_doc)

print("fin")











