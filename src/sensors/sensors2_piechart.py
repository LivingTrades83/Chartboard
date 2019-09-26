# -*- coding: utf-8 -*-
import datetime, json, requests, time
from src.tipboard.app.properties import TIPBOARD_URL
from src.sensors.utils import getTimeStr, end, sendBVColor

NAME_OF_SENSORS = "GET"
TILE_TEMPLATE = "pie_chart"
TILE_ID = "pie_ex"

def executeScriptToGetData():
    """ Simulate some actions for text tile exemple"""
    return {
        "title": "My title",
        "pie_data": [["Pie 1", 25],
                     ["Pie 2", 25],
                     ["Pie 3", 50]]
    }


def sendDataToTipboard(data=None, tile_template=None, tile_id="", isTest=False):
    configTile = {
        "tile": tile_template, #tile_template name
        "key": tile_id, #tile_template name
        "data": json.dumps(data)
    }
    if not isTest:
        res = requests.post(TIPBOARD_URL + "/push", data=configTile)
    print(f"{res} -> {tile_id}: {res.text}", flush=True)

def sonde2(isTest):
    start_time = time.time()
    data = executeScriptToGetData()
    sendDataToTipboard(data, tile_template=TILE_TEMPLATE, tile_id=TILE_ID, isTest=isTest)
    end(title=f"sensors2 -> {TILE_ID}", start_time=start_time)