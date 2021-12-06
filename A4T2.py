from os import lseek
from pymongo import MongoClient
from bson.json_util import loads
import json
import datetime  

client = MongoClient('mongodb://localhost:27017')


# Create or open the video_store database on server.
db = client["A4dbEmbed"]


# List collection names.
collist = db.list_collection_names()

# Create or open the collection in the db
ArtistsTracks = db["ArtistsTracks"]
ArtistsTracks.delete_many({})
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

result = db.Artists.aggregate([
{
'$lookup':{
            'localField': "tracks",
            'from':"Tracks",        
            'foreignField': "track_id",
            'as': "tracks"        
        }
}
])

for n in result:
    ArtistsTracks.insert_one(n)

artists.drop()
tracks.drop()