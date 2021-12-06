from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')

db = client["A4dbEmbed"]

result = db.ArtistsTracks.aggregate([
    {"$match": {
        "tracks.duration": {"$exists": True}
        }
    },
    {"$project": 
        {"_id": 1,
        "total_length": {"$sum": "$tracks.duration"},
        "artist_id": 1
        }
    }
])
for i in result:
    print(i)


