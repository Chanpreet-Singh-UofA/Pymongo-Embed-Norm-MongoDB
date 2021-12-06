from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')

db = client["A4dbNorm"]

result = db.Tracks.aggregate([
    {"$match": {
        "duration": {"$exists": True}
        }
    },
    {"$project": 
        {"_id": 1,
        "total_length": {"$sum": "$duration"},
        "artist_id": "$artist_ids"
        }
    }
])
for i in result:
    print(i)
