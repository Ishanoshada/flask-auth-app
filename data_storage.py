import json
from pymongo import MongoClient

# Change this variable to "json" if you want to use JSON as the data storage method,
# or to "pymongo" if you want to use MongoDB.
data_storage_method = "json"

if data_storage_method == "pymongo":
    # Connect to the MongoDB server running on localhost
    client = MongoClient('mongodb://localhost:27017/')
    # Access the 'my_auth_app' database
    db = client['my_auth_app']
    # Access the 'users' collection within the database
    users_collection = db['users']

def load_users():
    if data_storage_method == "json":
        try:
            # Attempt to open and read user data from the 'users.json' file
            with open('users.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            # If the file doesn't exist, return an empty list
            return []
    elif data_storage_method == "pymongo":
        # If using MongoDB, retrieve user data from the 'users_collection'
        users = []
        for user in users_collection.find():
            users.append(user)
        return users

def save_users(users):
    if data_storage_method == "json":
        # If using JSON, write user data to the 'users.json' file
        with open('users.json', 'w') as file:
            json.dump(users, file)
    elif data_storage_method == "pymongo":
        # If using MongoDB, clear existing data and insert provided users into the 'users_collection'
        users_collection.delete_many({})
        users_collection.insert_many(users)
      
