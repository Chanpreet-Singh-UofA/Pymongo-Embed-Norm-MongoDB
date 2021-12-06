from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')

db = client["A4dbEmbed"]

result = db.ArtistsTracks.aggregate([
    {
      "$unwind" : "$tracks"
    },
    {"$match": {
        "tracks.track_id": { "$regex": "^70" }
        }
    },
    {
        "$group":{
            "_id": "",
            "avg_danceability": {"$avg": "$tracks.danceability"}
        }
    }
])

for i in result:
    print(i)