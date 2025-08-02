from typing import Collection
import motor.motor_asyncio
import os
from dotenv import load_dotenv

load_dotenv()

# Use MongoDB Atlas cluster connection string
MONGO_URI = "mongodb+srv://isurudidulantha:Didu12345@cluster0.sdrbhn0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
print(f"MongoDB URI: {MONGO_URI}")

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)

#database
database = client.get_database("braindump")
print(f"Connected to database: {database.name}")


#collections
Collection_user = database["user"]
