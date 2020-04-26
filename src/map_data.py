"""
file: map_data.py
author: Isaac Perper
created: 04/25/2020

Creates list of map markers at each national park.
"""

import json
import pathlib
import logging
import re

from db_handler import ParkDB, sqlite3
from map import make_map

base_dir = pathlib.Path(__file__).parent.absolute()

key_file = base_dir / "../keys/secrets.json"
alert_db = base_dir / "../db/park_alerts.db"
park_file = base_dir / "../db/park_codes.json"
map_file = base_dir / "../maps/NPSCovidMap.html"

def get_closure_alerts(alert_list):
    """
    Returns only the alerts that have a closure label
    """
    out = []
    for alert in alert_list:
        if alert[2] == "Park Closure":
            out.append(alert)
    return out

def get_waypoint_info(park_id, DB):
    """
    Creates the dictionary of required info for the map marker
    given a park id. 

    If there is no closure alert for the park, it assumes the park is open.
    """
    info = {}
    # (code, name, lon, lat, url)
    park_info = DB.get_park_info(park_id)
    # [(code, title, alert_type, description), (...), ...]
    alert_info = DB.get_alert_info(park_id)
    
    if park_info is None:
        logging.error("Park ID: %s is not in DB", park_id)
        return None

    if park_info[2] == '' or park_info[3] == '':
        logging.warning("Park has no long lat, skipping")
        return None
    
    info["name"] = park_info[1].replace("`","")
    info["lon"] = park_info[2]
    info["lat"] = park_info[3]
    info["url"] = park_info[4].replace("`","")


    # If no alert for part, assume open
    if alert_info is None:
        info["status"] = "open"
        info["desc"] = "No closure updates from this park"
        return info
    else:
        # Multiple possible alerts for given park
        closure_alerts = get_closure_alerts(alert_info)
        closed_words = {"closure", "closed", "close", "closing"}
        open_words = {"open"}
        includes_open, includes_closed = False, False
        for alert in closure_alerts:
            description = alert[3]
            # If any of the open words are in the description, then the park 
            # could be open. 
            if any(word in open_words for word in description.lower().split()):
                includes_open = True
            # If any of the closed words are in description, but open words weren't
            # then status is closed.
            if any(word in closed_words for word in description.lower().split()):
                includes_closed = True
            
        if includes_open and not includes_closed:
            # If only open, then open
            info["status"] = "open"
            info["desc"] = "\n".join([alert[3].replace("`", "") for alert in closure_alerts])
        elif not includes_open and includes_closed:
            # If only closed, then closed
            info["status"] = "closed"
            info["desc"] = "\n".join([alert[3].replace("`", "") for alert in closure_alerts])
        else:
            # If both open and closed, or neither, then other
            info["status"] = "other"
            info["desc"] = "\n".join([alert[3].replace("`", "") for alert in closure_alerts])

        return info

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logging.info("Running map_data.py")

    # # Load API key from file
    # with open(key_file,  'r', encoding='utf-8') as f_secret:
    #     api_key = json.load(f_secret)["nps_api"]

    with open(park_file, 'r', encoding='utf-8') as f_codes:
        park_dict = json.load(f_codes)
    park_codes = list(park_dict.keys())

    # Create DB object
    DB = ParkDB(alert_db)

    closed_map_info = []
    open_map_info = []
    other_map_info = []
    for i, park in enumerate(park_codes):
        info = get_waypoint_info(park, DB)
        if info is not None:
            if info["status"] == "closed":
                closed_map_info.append(info)
            elif info["status"] == "open":
                open_map_info.append(info)
            elif info["status"] == "other":
                other_map_info.append(info)

    map_info = closed_map_info + open_map_info + other_map_info
    print(len(map_info))

    logging.info("Created map data. Now generating map")

    make_map(map_info, str(map_file))
        



    