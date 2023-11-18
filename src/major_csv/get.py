from dotenv import load_dotenv
import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

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

def get_department():
    db = client["erode"]
    print("connected to Database 'erode' successfully!")

    department_collection = db['department']
    department_docs = department_collection.find({})

    for doc in department_docs:
        department, college = doc.get('_id'), doc.get('college')
        print(f'학과 : {department} | 대학: {college}')

def get_user_major():
    user_major = input("당신의 전공은 무엇입니까? : ")
    second_major = input("복수 전공을 할 예정인가요? ( yes / no ) : ")
    
    if second_major.lower() == "yes":
        user_second_major = input("당신의 복수 전공은 무엇입니까? : ")
    elif second_major.lower() == "no":
        print("복수전공을 선택하지 않습니다.")
        user_second_major = "none"
    else:
        print("Invalid Input. please enter yes or no")
        exit()
    
    print(f'전공: {user_major} | 복수전공 : {user_second_major}')

    return user_major, user_second_major

def get_Libral_arts():
    return 0


def get_first_major(user_major):
    return 0

get_department()
get_user_major()