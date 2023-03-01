"""
Nose tests for mypymongo.py

Write your tests HERE AND ONLY HERE.
"""

from acp_times import open_time, close_time
from mypymongo import brevet_display, brevet_submit
import nose  # Testing framework
import logging
import os
from pymongo import MongoClient
import arrow

logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.WARNING)
log = logging.getLogger(__name__)

client = MongoClient('mongodb://' + os.environ['MONGODB_HOSTNAME'], 27017)
db = client.mydb
collection = db.lists


def test_submit():
    start_time = "2023-02-17T00:00"
    brevet_dist = 200
    controls = {"km": 100,
                "miles": 62.137100,
                "open": "2023-02-17T00:00",
                "close": "2023-02-17T06:40"}

    brevet_submit(start_time, brevet_dist, controls)
    # use find and compare values
    data = [x for x in collection.find()]

    newest_input = data[len(data) - 1]

    assert newest_input["start_time"] == start_time
    assert newest_input["brevet_dist"] == brevet_dist
    assert newest_input["controls"]["km"] == controls["km"]
    assert newest_input["controls"]["miles"] == controls["miles"]
    assert newest_input["controls"]["open"] == controls["open"]
    assert newest_input["controls"]["close"] == controls["close"]


def test_display():
    start_time = "2023-02-17T00:00"
    brevet_dist = 200
    controls = {"km": 100,
                "miles": 62.137100,
                "open": "2023-02-17T00:00",
                "close": "2023-02-17T06:40"}

    collection.insert_one({
        "start_time": start_time,
        "brevet_dist": brevet_dist,
        "controls": controls})

    dis_start_time, dis_brevet_dist, dis_controls = brevet_display()

    # assert that they equal
    assert start_time == dis_start_time
    assert brevet_dist == dis_brevet_dist
    assert controls["km"] == dis_controls["km"]
    assert controls["miles"] == dis_controls["miles"]
    assert controls["open"] == dis_controls["open"]
    assert controls["close"] == dis_controls["close"]
