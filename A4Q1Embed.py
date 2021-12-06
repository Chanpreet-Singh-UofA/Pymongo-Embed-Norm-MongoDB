from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')

db = client["A4dbEmbed"]

result = db.ArtistsTracks.aggregate([
    {"$match": {
        "tracks": {"$exists": True},
        "$nor": [{"tracks": {"$size": 0}}]
        }
    },
    {"$project": 
        {"_id": 1,
         "artist_id": 1,
         "name": 1,
        "number of tracks" : { "$size": "$tracks"}
        }
    }
])

for i in result:
    print(i)
