from pymongo import MongoClient
import json

client = MongoClient('mongodb://localhost:27017')

db = client["A4dbNorm"]

result = db.Artists.aggregate([
    {"$match": {
        "tracks": {"$exists": True},
        "$nor": [{"tracks": {"$size": 0}}]
        }
    },
    {"$project": 
        {"_id": 1,
         "artist_id": 1,
         "name": 1,
        "num_tracks" : { "$size": "$tracks"}
        }
    }
])

for i in result:
    print(i)


