
from os import lseek
from pymongo import MongoClient
from bson.json_util import loads
import json
import datetime  

# Use client = MongoClient('mongodb://localhost:27017') for specific ports!
# Connect to the default port on localhost for the mongodb server.
client = MongoClient('mongodb://localhost:27017')


db = client["A4dbNorm"]

# Create or open the collection in the db

artists = db["Artists"]
artists.delete_many({})
tracks = db["Tracks"]
tracks.delete_many({})


#https://www.geeksforgeeks.org/how-to-import-json-file-in-mongodb-using-python/
with open('artists.json') as file:
    artists_data = json.load(file)


for record in artists_data:
    record["_id"] = record["_id"]["$oid"]


artists.insert_many(artists_data)

with open('tracks.json') as file:
    tracks_data = json.load(file)

for record2 in tracks_data:
    record2["_id"] = record2["_id"]["$oid"]
    if "$numberLong" in record2["release_date"]["$date"]:
        dateissue = int(record2["release_date"]["$date"]["$numberLong"])
        convdate = dateissue/1000
        record2["release_date"] = datetime.datetime.fromtimestamp(convdate)
    else:
        record2["release_date"] = record2["release_date"]["$date"]

tracks.insert_many(tracks_data)
