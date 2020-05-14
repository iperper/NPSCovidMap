"""
file: db_handler.py
author: Isaac Perper
created: 04/25/2020

Handles the park alert database via the ParkDB class.
"""

import sqlite3

class ParkDB:
    """
    Contains methods for interacting with the stored NPS alerts
    """
    def __init__(self, db_file):
        self.db_file = str(db_file)

        # Initialize tables if needed
        self.create_alert_tables()

    def create_connection(self):
        """ Creates sqlite connection with db_file """
        conn = None
        try:
            conn = sqlite3.connect(self.db_file)
            return conn
        except sqlite3.Error as e:
            print(e)
        return conn

    def execute(self, sql, args=tuple(), fetch=None):
        """
            Creates connection, runs sql, and closes connection
            SQL commands can contain parameters via ?, which are
            passed in via a tuple args.

            Delay closing if you want to get response.
        """
        conn = self.create_connection()
        if conn is not None:
            c = conn.cursor()
            if fetch is None:
                response = c.execute(sql, args)
            elif fetch == "all":
                response = c.execute(sql, args).fetchall()
            elif fetch == "one":
                response = c.execute(sql, args).fetchone()
            conn.commit()
            conn.close()
            return response
        else:
            raise sqlite3.Error("Database connection could not be established.")

    def create_alert_tables(self):
        """Creates table needed to store alert data"""
        parks_table = """CREATE TABLE IF NOT EXISTS parks (
                code text,
                name text,
                lon real,
                lat real,
                url text
                );"""
        alerts_table = """CREATE TABLE IF NOT EXISTS alerts (
                code text,
                title text,
                alert_type text,
                description text
                );"""
        try:
            self.execute(parks_table)
            self.execute(alerts_table)
        except sqlite3.Error as e:
            print(e)
            print("Could not create tables. Check db files.")

    def insert_park(self, code, name, lon, lat, url, replace=False):
        """
        Creates new entry into park table.
        """
        park_info = self.get_park_info(code)
        if (not replace) and (park_info is not None):
            # If already in DB, don't re-add
            return 0
        
        if (not replace) or (replace and park_info is None):
            sql = """INSERT INTO parks (code, name, lon, lat, url)
                VALUES(?,?,?,?,?);"""
            args = (code, name, lon, lat, url)
        else:
            sql = """UPDATE parks SET code = ?, name = ?, lon = ?, lat = ?, url = ?
                WHERE code = ?;"""
            args = (code, name, lon, lat, url, code)

        self.execute(sql, args)
        return 1

    def insert_alert(self, code, title, alert_type, description, replace=False):
        """
        Creates new entry into alert table
        """
        alert_info = self.get_alert_info(code, title)
        if not replace and alert_info is not None:
            # If already in DB, don't re-add
            return 0
        
        if (not replace) or (replace and alert_info is None):
            sql = """INSERT INTO alerts (code, title, alert_type, description)
                VALUES(?,?,?,?);"""
            args = (code, title, alert_type, description)
        else:
            sql = """UPDATE alerts SET code = ?, title = ?, alert_type = ?, description = ?
                WHERE code = ? AND title = ?;"""
            args = (code, title, alert_type, description, code, title)
        self.execute(sql, args)
        return 1
    
    def get_park_info(self, park_id):
        """ Returns park info in DB given park_id.  None if no park exists. """
        sql = """SELECT * FROM parks WHERE code = ?;"""
        response = self.execute(sql, (park_id, ), fetch="one")
        return response
   
    def get_alert_info(self, park_id, title=None):
        """
        Returns alert info in DB given park_id.  None if no alert exists.
        If title is specifid, return one repsonse. If no title, then returns
        all alerts associated with park_id
        """
        if title is not None:
            sql = """SELECT * FROM alerts WHERE code = ? AND title = ?;"""
            response = self.execute(sql, (park_id, title), fetch="one")
        else:
            sql = """SELECT * FROM alerts WHERE code = ?;"""
            response = self.execute(sql, (park_id,), fetch="all")
        return response

    def get_parks_table(self):
        sql = """SELECT * FROM parks;"""
        return self.execute(sql, fetch="all")

    def get_alerts_table(self):
        sql = """SELECT * from alerts;"""
        return self.execute(sql, fetch="all")

    def get_all_tables(self):
        return (self.get_parks_table(), self.get_alerts_table())