from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')

db = client["A4dbNorm"]

result = db.Tracks.aggregate([
    {"$match": {
        "track_id": { "$regex": "^70" }
        }
    },
    {
        "$group":{
            "_id": "",
            "avg_danceability": {"$avg": "$danceability"}
        }
    }
])

for i in result:
    print(i)
