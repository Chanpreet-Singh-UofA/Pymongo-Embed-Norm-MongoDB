from pymongo import MongoClient
from datetime import datetime

client = MongoClient('mongodb://localhost:27017')

db = client["A4dbEmbed"]


result = db.ArtistsTracks.aggregate([
    {
      "$unwind" : "$tracks"
    },
    {
        "$addFields": {
            "convertedDate": { "$toDate": "$tracks.release_date" }
        }
    }
])

datetime_object = datetime(1950, 1, 1, 0, 0)

result = db.ArtistsTracks.aggregate([
    {
      "$unwind" : "$tracks"
    },
    {"$match": {
        "tracks.release_date": { "$gte" : datetime_object }
        }
    },
    {"$project": 
        {"_id": 0,
         "name": 1,
         "tracks.name": 1,
         "tracks.release_date": 1
        }
    }
])

for i in result:
    print(i)
