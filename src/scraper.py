"""
file: scraper.py
author: Isaac Perper
created: 04/25/2020

Pulls and stores alert info from National Park Service API
"""

import requests
import json
import pathlib
import logging

from db_handler import ParkDB, sqlite3

base_dir = pathlib.Path(__file__).parent.absolute()

key_file = base_dir / "../keys/secrets.json"
alert_db = base_dir / "../db/park_alerts.db"
park_file = base_dir /"../db/park_codes.json"

def get_response(endpoint, args, timeout=0.001):
    '''
    Takes endpoint and query and returns data from get request.
    Params:
        - endpoint (str): where API call is directed
        - args (dict): dictionary in json format of arguments
    Returns:
        - python 'Requests' object from get request
    Example:
        get_response(alerts, {"parkCode": "yell", "statecode"="MO,CA")
    '''
    url = "https://developer.nps.gov/api/v1/"
    url += endpoint
    args["api_key"] = api_key
    logging.debug("Sent GET request")
    try:
        r = requests.get(url, args, timeout=timeout)
        r.raise_for_status
        return r
    except requests.exceptions.MissingSchema:
        logging.error("Request URL invalid.")
        return None
    except requests.exceptions.HTTPError:
        logging.error("Bad request.")
        return None

# def parse_alerts(**kwargs):

def dump_json(filename, response):
    '''
    Saves responses to file so large requests aren't mad repeatedly.
    Assumes response has JSON format.
    '''
    try:
        with open(base_dir/ 'db' / filename, 'w', encoding='utf-8') as f:
            json.dump(response.json(), f, ensure_ascii=False, indent=4)
        logging.info("Response was saved successfuly to %s", base_dir/ 'db' / filename)
        return True
    except ValueError:
        logging.error("Response has no JSON format. No file saved.")

def get_all_alerts(n=1000):
    alert_args = {"parkCode": "", 'stateCode': "", "limit": str(n), "start":"1" }
    # Note the long timeout due to large request
    try:
        return get_response('alerts', alert_args, timeout=2)
    except requests.exceptions.ReadTimeout as e:
        logging.error(e)
        return None

def get_all_parks(n=1000):
    park_args = {"parkCode": "", 'stateCode': "", "limit": str(n), "start":"1" }
    # Note the long timeout due to large request
    try:
        return get_response('parks', park_args, timeout=str(n))
    except requests.exceptions.ReadTimeout as e:
        logging.error(e)
        return None

def get_parks(park_codes):
    """
    Returns park info for each park listed in park_codes
    """
    park_args = {"parkCode": ",".join(park_codes), "limit": str(len(park_codes))}
    try:
        return get_response('parks', park_args, timeout=3+1*len(park_codes))
    except requests.exceptions.ReadTimeout as e:
        logging.error(e)
        return None

def parse_parks_to_DB(data, DB):
    """
    Adds all the parks to to the db
    """
    for i, park in enumerate(data):
        try:
            DB.insert_park(park["parkCode"], park["name"], park["longitude"], park["latitude"], park["url"])
        except sqlite3.Error as e:
            logging.error(e)
            logging.error("Only added first %d entries from data.", i-1)
    return True

def parse_alerts_to_DB(data, DB):
    """
    Adds all the alerts to to the db
    """
    for i, alert in enumerate(data):
        try:
            DB.insert_alert(alert["parkCode"], alert["title"], alert["category"], alert["description"])
        except sqlite3.Error as e:
            logging.error(e)
            logging.error("Only added first %d entries from data.", i-1)
    return True

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    logging.info("Running")

    # Load API key from file
    with open(key_file) as f_secret:
        api_key = json.load(f_secret)["nps_api"]

    with open(park_file) as f_codes:
        park_dict = json.load(f_codes)

    park_codes = list(park_dict.keys())
    
    # r = get_all_alerts(5)
    # r2 = get_all_parks(5)
    # logging.info("Got alert")

    DB = ParkDB(alert_db)


