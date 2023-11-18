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

db = client['erode']
course_collection = db['course']
courseIntro_collection = db['course_intro']

# ci , dm, m file path recusive
print("...Getting file pahts...")
root = input("root : ") # all files must be nested in the root folder
output_path = root+"/"+input("output folder name: ")+"/" # exported csv files goes here

os.makedirs(output_path,exist_ok=True)

print("...Getting course introductions...")
ci_pdf_files = Path(root).rglob('교과목기술_*.pdf')
for idx, path in enumerate(ci_pdf_files):
    path = str(path)
    ci_csv_name = path.split('/')[-1].split('.')[0]+".csv"
    df = csv_func.transform_funcs.course_intro_df(path, ci_csv_name , output_path)
    ci_course_docs = csv_func.transform_funcs.ci_course_doc(df)
    ci_courseintro_docs = csv_func.transform_funcs.ci_course_intro_doc(df)
    if 













