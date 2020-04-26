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
        return get_response('alerts', alert_args, timeout=n)
    except requests.exceptions.ReadTimeout as e:
        logging.error(e)
        return None

def get_alerts(park_codes):
    """
    Returns alert info for each park listed in park_codes
    """
    alert_args = {"parkCode": ",".join(park_codes), "limit": 5*str(len(park_codes))}
    try:
        return get_response('alerts', alert_args, timeout=20*len(park_codes))
    except requests.exceptions.ReadTimeout as e:
        logging.error(e)
        return None

def get_all_parks(n=1000):
    """
    Gets info from all the parks. 
    TODO: Currently takes too long to run.  Running individually
    """
    park_args = {"parkCode": "", 'stateCode': "", "limit": str(n), "start":"1" }
    # Note the long timeout due to large request
    try:
        return get_response('parks', park_args, timeout=n)
    except requests.exceptions.ReadTimeout as e:
        logging.error(e)
        return None

def get_parks(park_codes):
    """
    Returns park info for each park listed in park_codes
    """
    park_args = {"parkCode": ",".join(park_codes), "limit": str(len(park_codes))}
    try:
        return get_response('parks', park_args, timeout=3+5*len(park_codes))
    except requests.exceptions.ReadTimeout as e:
        logging.error(e)
        return None

def parse_parks_to_DB(data, DB):
    """
    Adds all the parks to to the db
    """
    for i, park in enumerate(data):
        try:
            resp = DB.insert_park(park["parkCode"], park["name"], park["longitude"], park["latitude"], park["url"])
            if resp == 0:
                logging.info("%s already in DB", park["parkCode"])
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
            resp = DB.insert_alert(alert["parkCode"], alert["title"], alert["category"], alert["description"])
            if resp == 0:
                logging.info("%s already in DB", alert["parkCode"])
        except sqlite3.Error as e:
            logging.error(e)
            logging.error("Only added first %d entries from data.", i-1)
    return True

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logging.info("Running")

    # Load API key from file
    with open(key_file) as f_secret:
        api_key = json.load(f_secret)["nps_api"]

    with open(park_file) as f_codes:
        park_dict = json.load(f_codes)
    park_codes = list(park_dict.keys())

    # Create DB object
    DB = ParkDB(alert_db)

    # Get all the Parks into the database
    #  Minimize API calls without calling all parks at once
    start = 0
    missed = set()
    group_size = 10
    park_codes_grouped = [park_codes[group_size*i:min(group_size*i+10, len(park_codes))] for i in range(start, len(park_codes)//group_size + 1)]
    # for i, group in enumerate(park_codes_grouped):
    #     logging.info("Getting Park Info for group %d", i)
    #     park_info = get_parks(group)
    #     if park_info is not None:
    #         logging.info("Getting info succeeded for %d", i)
    #         parse_parks_to_DB(park_info.json()['data'], DB)
    #     else:
    #         logging.info("Getting info failed for %d", i)
    #         missed.add(i)
    # logging.info("Missed parks %s", str(missed))
    # logging.info("Added non-missed parks to parks table")

    # for i, group in enumerate(park_codes_grouped):
    #     logging.info("Getting Park Info for group %d", i)
    #     alert_info = get_alerts(group)
    #     if alert_info is not None:
    #         logging.info("Getting info succeeded for %d", i)
    #         parse_alerts_to_DB(alert_info.json()['data'], DB)
    #     else:
    #         logging.info("Getting info failed for %d", i)
    #         missed.add(i)

    # logging.info("Missed alerts from parks: %s", str(missed))
    # logging.info("Added non-missed alerts to alerts table")
