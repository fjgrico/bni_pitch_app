from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.getenv("MONGODB_URI"))
db = client[os.getenv("DB_NAME")]
users_collection = db[os.getenv("USERS_COLLECTION")]
pitch_collection = db[os.getenv("PITCH_COLLECTION")]

def save_user_data(user_id, name, company, membership):
    users_collection.update_one(
        {"_id": user_id},
        {"$set": {"name": name, "company": company, "membership": membership}},
        upsert=True
    )

def load_user_data(user_id):
    return users_collection.find_one({"_id": user_id})

def save_pitch_data(user_id, pitch_text):
    pitch_collection.insert_one({
        "user_id": user_id,
        "pitch": pitch_text
    })