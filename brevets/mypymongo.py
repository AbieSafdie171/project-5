import os
from pymongo import MongoClient

client = MongoClient('mongodb://' + os.environ['MONGODB_HOSTNAME'], 27017)
db = client.mydb
collection = db.lists


def brevet_submit(start_time, brevet_dist, controls):

    # inputs into database
    output = collection.insert_one({
        "start_time": start_time,
        "brevet_dist": brevet_dist,
        "controls": controls})
    _id = output.inserted_id
    return str(_id)


def brevet_display():
    # receives the list from the database
    lists = collection.find().sort("_id", -1).limit(1)

    # returns the necessary data
    for brevet in lists:
        return brevet["start_time"], brevet["brevet_dist"], brevet["controls"]
