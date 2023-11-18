import os
import tabula
import pandas as pd
from dotenv import load_dotenv
import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

root = '/Users/yhjune/Desktop/playground/pdf/'
output_path = root+'resutls/'
os.makedirs(output_path,exist_ok=True)

ci_pdf_path = root+'major_origin/경영대학/교과목기술_경영학부.pdf'
ci_csv_name = ci_pdf_path.split('/')[-1].split('.')[0]+".csv"

def course_intro_df(ci_pdf_path, ci_csv_name, output_path):
    msg = "course introduction"
    
    df = tabula.read_pdf(ci_pdf_path, pages= "all", lattice=True, area=[135.3, 15.3 ,563.6 , 822.5]) #PDF 읽어오기
    df_concat = pd.concat(df, ignore_index=True)

    df_concat.columns = ["순번","설정전공","_id","교과목명","교과목명(영문)","교과목기술(국문)","교과목기술(영문)"] # colums name

    df_concat.replace(r'\r','', regex=True ,inplace=True) # colum's deails
    df_concat.reset_index(drop=True, inplace=True)
    df_concat.drop(columns="순번")

    df_concat = df_concat[["_id","설정전공","교과목명","교과목명(영문)","교과목기술(국문)","교과목기술(영문)"]] # colum order

    df_concat.columns = ["course_id", "department_id", "course_name","course_name_eng","intro_kr","intro_eng"]
    df_concat['course_id'] = df_concat['course_id'].astype("int")
    df_concat = df_concat.astype("str")

    return df_concat

def ci_course_document(dataframe):
    new_courses = []

    for row in dataframe.itertuples():
        course_id, department_id, course_name = row.course_id, row.department_id, row.course_name
        course  ={ 
            "_id" : course_id,
            "department_id" : department_id,
            "name" : course_name,
            "classification": '',
            "credit": ''
        }
        new_courses.append(course)
    return new_courses

def ci_course_intro_document(dataframe):
    new_course_intros = []
    for row in dataframe.itertuples():
        course_id, department_id, course_name, course_name_eng, intro_kr, intro_eng = row.course_id, row.department_id, row.course_name, row.course_name_eng, row.intro_kr, row.intro_eng
        course_intro = {
            "_id":{
                "course_id" : course_id,
                "department_id" : department_id
            },
            "course_name" : course_name,
            "intro_kr": intro_kr ,
            "intro_eng": intro_eng ,
            "academic_year": '',
            "course_name_eng" : course_name_eng 
        }
        new_course_intros.append(course_intro)
    
    return new_course_intros

df = course_intro_df(ci_pdf_path, ci_csv_name, output_path)

ci_course_docs = ci_course_document(df)
ci_courseinro_docs = ci_course_intro_document(df)

print(ci_course_docs[1])
print(ci_courseinro_docs[1])
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

db = client['erode']
course_collection = db['course']
courseIntro_collection = db['course_intro']

# result2 = courseIntro_collection.insert_many(ci_courseinro_docs)

client.close()