import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.getenv("MONGODB_URI"))
db = client[os.getenv("DB_NAME")]
users_col = db[os.getenv("USERS_COLLECTION")]
pitch_col = db[os.getenv("PITCH_COLLECTION")]

def save_user_data(email, name, empresa, membresia):
    users_col.update_one({"email": email},
                         {"$set": {"name": name, "empresa": empresa, "membresia": membresia}},
                         upsert=True)

def load_user_data(email):
    data = users_col.find_one({"email": email})
    return data if data else {}

def save_pitch_data(email, pitch):
    pitch_col.insert_one({"email": email, "pitch": pitch})