from dotenv import load_dotenv
import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

def start_client():
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

    db = client["erode"]
    print("connected to Database 'erode' successfully!")

    return client, db